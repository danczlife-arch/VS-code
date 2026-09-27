print("Welcome to your shopping list!")

shopping_list = []

while True:
    print("\n--- SHOPPING LIST ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Exit")
    print("5. Clear list")
    print("6. Check if item is in the list")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to your shopping list.")

    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from your shopping list.")
        else:
            print(f"{item} is not in your shopping list.")

    elif choice == "3":
        print("\nYour shopping list:")
        
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

        print("Total items in the list:", len(shopping_list))
    elif choice == "4":
        print("Thank you for using the shopping list application! Goodbye!")
        break

    elif choice == "5":
        shopping_list.clear()
        print("Your shopping list has been cleared.")

    elif choice == "6":
        item = input("Enter the item to check: ")
        if item in shopping_list:
            print(f"{item} is in your shopping list.")
        else:
            print(f"{item} is not in your shopping list.")

    else:
        print("Invalid option. Please choose a number between 1 and 6.")   