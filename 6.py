# 6. Write a program that reads the content of a text file and prints it to the console.
def read_from_file():

    file_name = "output.txt"

    try:

        with open(file_name, "r") as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")


read_from_file()