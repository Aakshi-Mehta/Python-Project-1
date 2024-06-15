# 5. Write a program that takes a string input from the user and writes it to a text file.

def write_to_file():

    user_input = input("Enter a string to write to the file: ")

    file_name = "output.txt"

    with open(file_name, "w") as file:
        file.write(user_input)

    print(f"The string has been written to {file_name}")

write_to_file()