# Removing items from a set

fruits = {"apple", "banana", "mango", "orange"}

# 1. discard() — removes item; no error if item not found
fruits.discard("banana")
print("After discard:", fruits)

# 2. remove() — removes item; gives error if item not found
fruits.remove("mango")
print("After remove:", fruits)

# 3. pop() — removes and returns a random item
removed_item = fruits.pop()
print("Popped item:", removed_item)
print("After pop:", fruits)
