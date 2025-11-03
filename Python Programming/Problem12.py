# Program to demonstrate in-built string functions

# Define a sample string
text = "  Hello World! Welcome to Python Programming.  "

print("Original String:")
print(text)

# 1. len() - Returns the length of the string
print("\n1. Length of string:", len(text))

# 2. lower() - Converts all characters to lowercase
print("\n2. Lowercase:", text.lower())

# 3. upper() - Converts all characters to uppercase
print("\n3. Uppercase:", text.upper())

# 4. title() - Converts first letter of each word to uppercase
print("\n4. Title Case:", text.title())

# 5. capitalize() - Capitalizes only the first letter of the string
print("\n5. Capitalized:", text.capitalize())

# 6. strip() - Removes spaces from the beginning and end
print("\n6. Strip spaces:", text.strip())

# 7. replace() - Replaces one substring with another
print("\n7. Replace 'World' with 'Everyone':", text.replace("World", "Everyone"))

# 8. split() - Splits the string into a list
print("\n8. Split string into list:", text.split())

# 9. join() - Joins list elements into a single string
words = ["Python", "is", "fun"]
print("\n9. Join list into string:", " ".join(words))

# 10. find() - Finds position of a substring (-1 if not found)
print("\n10. Find position of 'Python':", text.find("Python"))

# 11. count() - Counts occurrences of a substring
print("\n11. Count of 'o':", text.count('o'))

# 12. startswith() and endswith()
print("\n12. Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with '.':", text.strip().endswith("."))
