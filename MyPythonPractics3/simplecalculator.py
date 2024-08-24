def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    print(add(x, y))
elif operation == '-':
    print(subtract(x, y))
elif operation == '*':
    print(multiply(x, y))
elif operation == '/':
    print(divide(x, y))
else:
    print("Invalid operation")


#Simple Calculator
