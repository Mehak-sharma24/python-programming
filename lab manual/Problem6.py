num = int(input("Enter a number: "))
i = num
factorial = 1  

while i != 0:
    factorial *= i   
    i -= 1

print(f"Factorial of {num} is: {factorial}")
