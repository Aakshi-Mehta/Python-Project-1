# 26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def starts_with_prefix(string, prefix):
    return string.startswith(prefix)


def ends_with_suffix(string, suffix):
    return string.endswith(suffix)


user_string = input("Enter a string: ")


prefix = input("Enter a prefix to check if the string starts with it: ")

suffix = input("Enter a suffix to check if the string ends with it: ")


if starts_with_prefix(user_string, prefix):
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")


if ends_with_suffix(user_string, suffix):
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")