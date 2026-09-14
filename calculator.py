number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print("Sum: ", float(number1) + float(number2))
elif operation == "-":
    print("Difference: ", float(number1) - float(number2))
elif operation == "*":
    print("Multiplication: ", float(number1) * float(number2))
elif operation == "/":
    print("Division: ", float(number1) / float(number2))