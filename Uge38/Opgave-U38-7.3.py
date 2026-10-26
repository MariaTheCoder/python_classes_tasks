# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

# User provides one whole and positive number of their choice
number = int(input("Type in a number: "))

# We can use modulus to determine whether the provided number is a multiple of 10;
if number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The number is NOT a multiple of 10.")

