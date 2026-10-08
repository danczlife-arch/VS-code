import json
from pathlib import Path

transactions = []

DATA_FILE = Path(__file__).with_name("transactions.json")

if DATA_FILE.exists():
    with open(DATA_FILE, "r") as f:
        transactions = json.load(f)


def add_transaction(transaction_type):
    try:
        amount = float(
            input("Enter amount in CZK: ").replace(",", ".")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description
    }

    transactions.append(transaction)
    print("Transaction added!")


def show_transactions():
    if not transactions:
        print("No transactions yet.")
        return

    print("\n--- TRANSACTIONS ---")

    for i, transaction in enumerate(transactions, start=1):
        if transaction["type"] == "income":
            sign = "+"
        else:
            sign = "-"

        print(
            f"{i}. {sign}{transaction['amount']:.2f} CZK"
            f" | {transaction['category']}"
            f" | {transaction['description']}"
        )
def save_transactions():
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(transactions, file, ensure_ascii=False, indent=4)

    print("Transactions saved successfully!")
def load_transactions():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            transactions.extend(data)
        else:
            print("Saved data has an invalid format.")

    except FileNotFoundError:
        # Při prvním spuštění soubor ještě neexistuje.
        pass

    except json.JSONDecodeError:
        print("Could not read the saved file. Check its contents.")

def show_statistics():
    total_income = 0
    total_expenses = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        else:
            total_expenses += transaction["amount"]

    balance = total_income - total_expenses

    print("\n--- STATISTICS ---")
    print(f"Total income: {total_income:.2f} CZK")
    print(f"Total expenses: {total_expenses:.2f} CZK")
    print(f"Balance: {balance:.2f} CZK")

load_transactions()

while True:
    print("\n--- MONEY TRACKER ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show transactions")
    print("4. Show statistics")
    print("5. Save transactions")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_transaction("income")

    elif choice == "2":
        add_transaction("expense")

    elif choice == "3":
        show_transactions()
        
    elif choice == "4":
        show_statistics()

    elif choice == "5":
        save_transactions()
        print("Goodbye!")
        break
    
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Choose 1-6.")
