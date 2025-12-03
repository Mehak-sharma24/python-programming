class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

except ValueError:
    print("❌ Invalid input! Please enter a valid number.")

except NegativeNumberError as e:
    print("❌ Error:", e)

else:
    print(f"✅ You entered {num}, which is a valid positive number.")

finally:
    print("Program finished.")
