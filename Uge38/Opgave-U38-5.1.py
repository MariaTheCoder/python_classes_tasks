# Opgave 5-1.
# Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# * Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Car is pre-defined and we first evaluate whether the string equals exactly how it was defined which of course results in true
# Then we test it for another value which will always result in false unless we have already changed the value of variable car.

# * Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
age = 10

## Test for statements that should result in true
print('Test age == 10. I predict TRUE:', age == 10)
print('Test age > 9. I predict TRUE:', age > 9)
print('Test age >= 10. I predict TRUE:', age >= 10)
print('Test age != 18. I predict TRUE:', age != 18)
print('Test age < 18. I predict TRUE:', age < 18)

## Test for statements that should result in false
print('Test age == 18. I predict FALSE:', age == 18)
print('Test age > 20. I predict FALSE:', age > 20)
print('Test age >= 18. I predict FALSE:', age >= 18)
print('Test age != 10. I predict FALSE:', age != 10)
print('Test age < 9. I predict FALSE:', age < 9)