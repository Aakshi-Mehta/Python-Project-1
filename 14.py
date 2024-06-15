# 14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines


def read_multiple_lines():
    lines = []
    print("Enter multiple lines of text (press Enter on an empty line to finish):")

    while True:

        line = input()
        if line == "":
            
            break
        lines.append(line)


    print("\nYou entered:")
    for line in lines:
        print(line)



read_multiple_lines()