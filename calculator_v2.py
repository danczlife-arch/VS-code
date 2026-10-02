try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

except ValueError:
    print("Please enter numbers only.")
    exit()
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print("Sum: ", number1 + number2)

elif operation == "-":
    print("Difference: ", number1 - number2)

elif operation == "*":
    print("Multiplication: ", number1 * number2)

elif operation == "/":
    print("Division: ", number1 / number2)