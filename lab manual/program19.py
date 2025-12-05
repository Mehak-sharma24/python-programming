# List methods example

fruits = ["apple", "banana", "mango", "banana", "orange"]

# 1. count() - count occurrences
print("Count of 'banana':", fruits.count("banana"))

# 2. index() - find index of element
print("Index of 'mango':", fruits.index("mango"))

# 3. extend() - add elements from another list
more_fruits = ["grapes", "papaya"]
fruits.extend(more_fruits)
print("After extend:", fruits)

# 4. pop() - remove and return last element
removed_item = fruits.pop()
print("Popped item:", removed_item)
print("After pop:", fruits)

# 5. clear() - remove all elements
fruits.clear()
print("After clear:", fruits)
