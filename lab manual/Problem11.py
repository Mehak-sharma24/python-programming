# Program to demonstrate different string operators

# Defining two strings
str1 = "Hello"
str2 = "World"

print("String 1:", str1)
print("String 2:", str2)

# 1. Concatenation (+)
print("\n1. Concatenation (+):")
result = str1 + " " + str2
print("Result:", result)

# 2. Repetition (*)
print("\n2. Repetition (*):")
result = str1 * 3
print("Result:", result)

# 3. Membership Operators (in / not in)
print("\n3. Membership Operators (in / not in):")
print("'H' in str1:", 'H' in str1)
print("'z' not in str2:", 'z' not in str2)

# 4. String Slicing [:]
print("\n4. String Slicing [:]:")
print("str1[0:3]:", str1[0:3])   # first 3 characters
print("str2[1:]:", str2[1:])     # from index 1 to end
print("str2[-3:]:", str2[-3:])   # last 3 characters

# 5. String Comparison (==, !=, >, <)
print("\n5. String Comparison Operators:")
print("str1 == str2:", str1 == str2)
print("str1 != str2:", str1 != str2)
print("str1 > str2:", str1 > str2)   # compares lexicographically
print("str1 < str2:", str1 < str2)

print("\nProgram finished successfully!")

