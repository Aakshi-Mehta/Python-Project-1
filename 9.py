#9. Write a python program that checks if a substring is present in a given string.


main_string = input("Please enter the main string: ")

substring = input("Please enter the substring to check: ")

if substring in main_string:
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")