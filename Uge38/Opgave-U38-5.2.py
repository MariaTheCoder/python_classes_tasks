# Opgave 5-2.
# More Conditional Tests: You don’t have to limit the number of tests you create to 10.
# If you want to try more comparisons, write more tests and add them to conditional_tests.py.
# Have at least one True and one False result for each of the following:

car = "BMW"
year = 2022

# * Tests for equality and inequality with strings
print('Test car == "bmw". I predict FALSE:', car == "bmw")
print('Test car != "audi". I predict TRUE:', car != "audi")

# * Tests using the lower() method
print('Test car == "bmw".upper(). I predict TRUE:', car == "bmw".upper())
print('Test car == "bmw".lower(). I predict FALSE:', car == "bmw".lower())

# * Numerical tests involving equality and inequality, greater than and less than,
# greater than or equal to, and less than or equal to
print('Test year >= 2016. I predict TRUE:', year >= 2016)
print('Test year < 2014. I predict FALSE:', year < 2014)

# * Tests using the 'and' keyword and the 'or' keyword
if year > 2016 and car == "bmw".upper() or car == "audi".upper():
    print("Amazing deal!")
elif year > 2016 and car == "bmw".upper() or car == "audi".upper():
    print("Still a good deal.")
else:
    print("Perhaps a better deal exists out there...")

# * Test whether an item is in a list
car_brands = ["BMW", "AUDI", "TOYOTA", "VW"]

for car_brand in car_brands:
    if car_brand.lower() == car.lower():
        print("\nThis car exists in the list!")
        break

# * Test whether an item is not in a list
# Let assign a new value to the variable 'car'
# car = "KIA"

count = 0

for car_brand in car_brands:
    if car_brand == car:
        count += 1

if count == 0:
    print(f"\nThis car brand {car} does NOT exist in the list.")
else:
    print(f"\nThis car brand {car} does exist in the list!")