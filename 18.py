#18. Write a python program that checks if two strings are anagrams of each other.


string1 = input("Please enter the first string: ")


string2 = input("Please enter the second string: ")


# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()


    return sorted(str1) == sorted(str2)



if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")