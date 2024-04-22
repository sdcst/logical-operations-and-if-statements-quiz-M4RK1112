"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
is_hypotenuse = input("Is one of the numbers the hypotenuse of a right triangle? (yes/no): ").lower()
if is_hypotenuse == "yes":
    missing_side = (num1**2 - num2**2) ** 0.5
    print("The length of the missing side is:", round(missing_side, 1))
elif is_hypotenuse == "no":
    hypotenuse = (num1**2 + num2**2) ** 0.5
    print("The length of the hypotenuse is:", round(hypotenuse, 1))
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
