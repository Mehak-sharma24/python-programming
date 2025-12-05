# List operations using inbuilt functions

numbers = [40, 10, 30, 20, 50]

# 1. Find length of list
print("Length of list:", len(numbers))

# 2. Check if an element exists
print("Is 30 in list?", 30 in numbers)

# 3. Sort list
numbers.sort()
print("Sorted list:", numbers)

# 4. Reverse list
numbers.reverse()
print("Reversed list:", numbers)

# 5. Copy list
copy_list = numbers.copy()
print("Copied list:", copy_list)
