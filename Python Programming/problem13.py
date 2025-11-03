# Program to count vowels, consonants, digits, and length of a string

# Input string from user
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
length = 0

# Define vowels
vowel_letters = "aeiouAEIOU"

# Iterate through each character in the string
for char in text:
    if char.isalpha():  # Check if alphabet
        if char in vowel_letters:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():  # Check if digit
        digits += 1
    
    if not char.isspace():  # Count all non-space characters for length
        length += 1

# Display the results
print("\nResults:")
print("Total vowels:", vowels)
print("Total consonants:", consonants)
print("Total digits:", digits)
print("Length of string (excluding spaces):", length)
