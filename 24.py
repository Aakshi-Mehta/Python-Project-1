# 24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    return x / y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter the operator (+, -, *, /): ")


if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    if num2 == 0:
        result = "Error! Division by zero is not allowed."
    else:
        result = divide(num1, num2)
else:
    result = "Invalid operator entered."

# Print the result
print("Result:", result)
