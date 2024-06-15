# 22. Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    if len(numbers) == 0:
        return None, None
    else:
        return min(numbers), max(numbers)

user_input = input("Please enter a list of numbers, separated by spaces: ")

numbers_list = list(map(float, user_input.split()))

minimum, maximum = find_min_max(numbers_list)

if minimum is not None and maximum is not None:
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
else:
    print("The list is empty.")
