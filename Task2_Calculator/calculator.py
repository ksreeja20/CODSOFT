# Simple Calculator

# Ask the user to enter the first number
num1 = float(input("Enter first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter second number: "))

# Display the available operations
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Store the user's choice
choice = input("Enter your choice (1-4): ")

# Perform addition
if choice == "1":
    result = num1 + num2
    print("Result:", result)

# Perform subtraction
elif choice == "2":
    result = num1 - num2
    print("Result:", result)

# Perform multiplication
elif choice == "3":
    result = num1 * num2
    print("Result:", result)

# Perform division
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero is not allowed.")

# If the user enters anything other than 1, 2, 3, or 4
else:
    print("Invalid choice!")