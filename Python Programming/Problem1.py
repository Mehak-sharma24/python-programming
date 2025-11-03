num1 = int(input("Enter a nubmer: "))
num2 = int(input("Enter another number: ")) 

sum = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum}")

diff = num1 - num2
print(f"The difference between {num1} and {num2} is: {diff}")

product = num1 * num2
print(f"The product of {num1} and {num2} is: {product}")

if(num2 == 0):
    print("Zero is not allowed as denominator.")

else: 
    quo = num1/num2
    print(f"The Quotient of {num1} divided by {num2} is: {quo}")