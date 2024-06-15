#16. Write a program in python that counts the frequency of each character in a string.
user_string = input("Please enter a string: ")

frequency_dict = {}

for char in user_string:

    if char in frequency_dict:
        frequency_dict[char] += 1

    else:
        frequency_dict[char] = 1


print("Character frequency in the string:")
for char, frequency in frequency_dict.items():
    print(f"'{char}': {frequency}")