# A simple calculator program in Python

# Define the functions for the operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    else:
        return num1 / num2

# Take user input for the numbers and operation

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter the operation (+, -, *, /): ")

# Perform the selected operation

if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = subtract(num1, num2)
elif op == "*":
    result = multiply(num1, num2)
elif op == "/":
    result = divide(num1, num2)
else:
    result = "Error: Invalid operation"

# Display the result

print("Result: ", result)
