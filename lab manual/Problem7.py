num = int(input("Enter a number: "))
temp = num
n = len(str(num))
sum_of_power = 0
while(temp>0):
    remainder = temp % 10
    sum_of_power += remainder ** n
    temp //= 10

if sum_of_power == num: 
    print(f"{num} is an armstrong number.")

else:
    print(f"{num} is not an armstrong number.")