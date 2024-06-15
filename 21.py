# 21. Write a python program that counts the occurrences of a specific element in a list.

def count_occurrences():

    user_list = input("Enter the elements of the list separated by commas: ").split(',')

    user_list = [element.strip() for element in user_list]

    specific_element = input("Enter the element to count: ").strip()

    count = user_list.count(specific_element)

    print(f"The element '{specific_element}' occurs {count} times in the list.")


count_occurrences()