# Write a Python function called print_full_name that takes two strings:
# first → first name
# last → last name
# Your program should read the first name and last name from the user (one on each line), and then print this message:
# Hello firstname lastname! You just delved into python.
# Replace firstname and lastname with the actual names entered by the user.

def print_full_name(first, last):
    print(f"Hello {first} {last}! you just delved into python")

first= input()
last= input()
print_full_name(first,last)