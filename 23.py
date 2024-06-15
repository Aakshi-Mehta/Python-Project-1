# 23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


conversion_direction = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ").upper()

if conversion_direction == 'C':
    celsius_temp = float(input("Enter the temperature in Celsius: "))
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F.")
elif conversion_direction == 'F':
    fahrenheit_temp = float(input("Enter the temperature in Fahrenheit: "))
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C.")
else:
    print("Invalid input! Please enter 'C' or 'F' for the conversion direction.")