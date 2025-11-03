print("---Break Statement---")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i:", i)
        break  # Exits the loop when i = 5
    print(i)

print("---Pass statement---")
for i in range(1,10):
    if i == 6:
        pass
    print("Pass statement executed at i:",i)
    print(i)

print("---Continue statement---")
for i in range(1, 10):
    if i == 7:
        print("Skipping the value at i:",i)
        continue
    print(i)