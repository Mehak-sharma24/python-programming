base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent(power): "))

result = 1
count = 0

while(count<exponent):
    result *= base
    count += 1

print(f"{base} raised to the power {exponent} is {result}")

'''
num = int(input("Enter the base: "))
expo = int(input("Enter the power: "))

power = num**expo
print(power)
'''
