
# Taking two numbers as input from the user
print("=" * 50)
print("Basic Mathematical Operations Calculator")
print("=" * 50)

num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division with error handling for division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Displaying the results
print("\n" + "=" * 50)
print("RESULTS")
print("=" * 50)
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} × {num2} = {multiplication}")
print(f"Division: {num1} ÷ {num2} = {division}")
print("=" * 50)
