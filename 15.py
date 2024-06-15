#15. Write a program that reads data from a CSV file and prints it to the console.



import csv


# Function to read and print the content of a CSV file
def read_csv_file():

    file_name = "data.csv"

    try:

        with open(file_name, mode='r', newline='') as file:
            csv_reader = csv.reader(file)


            for row in csv_reader:
                print(row)

    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")


read_csv_file()