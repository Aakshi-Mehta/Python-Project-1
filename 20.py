# 20. Write a python program that takes a list of numbers and returns their sum.


def sum_of_numbers(numbers):
    return sum(numbers)


user_input = input("Please enter a list of numbers, separated by spaces: ")

numbers_list = list(map(float, user_input.split()))


total_sum = sum_of_numbers(numbers_list)


print("The sum of the numbers is:", total_sum)