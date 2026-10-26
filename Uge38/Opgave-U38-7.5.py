# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

# (Husk også at sørge for at man kan komme ud
# af loopet igen + sørg for at gemme og udskrive en totalpris for
# alle billetter til slut i programmet)

number_of_friends = int(input("Enter the number of friends: "))

ages = []
prices = []

count = 0

for i in range(number_of_friends):
    age = int(input("Enter age: "))
    ages.append(age)

# Test if the array looks correct
print("\nList of ages:", ages)

for age in ages:
    if age < 3:
        prices.append(0)
    elif age >= 3 and age <= 12:
        prices.append(10)
    else:
        prices.append(15)

print("List of prices:", prices)

total = 0

for price in prices:
    total += price

print("\nTotal price:", total)