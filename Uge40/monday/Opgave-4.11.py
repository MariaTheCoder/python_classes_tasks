# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.

favourite_pizzas = ['vegan kebab', 'vegan shawarma', 'vegan barbeque', 'vegan pepperoni', 'vegan verdura']

# for pizza in favourite_pizzas:
#    print(pizza)

# • Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should
# have one line of output containing a simple statement like I like pepperoni pizza.

# for pizza in favourite_pizzas:
#    print(f"One of my favourite pizzas is called '{pizza}'")

# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

# print("\nI really love pizza!")

# ==================================================================================

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
#
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
# following:

print("\nOpgave 4.11")

friend_pizzas = favourite_pizzas.copy()

# For good measure, print out the two lists
print(f"\nfavourite_pizzas: {favourite_pizzas}")
print(f"friend_pizzas: {friend_pizzas}")

# • Add a new pizza to the original list.
favourite_pizzas.append('vegan margherita pomodori')
# print(f"\nfavourite_pizzas: {favourite_pizzas}")
# print(f"friend_pizzas: {friend_pizzas}")

# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append('vegan bruschetta')
# print(f"\nfavourite_pizzas: {favourite_pizzas}")
# print(f"friend_pizzas: {friend_pizzas}")

# • Prove that you have two separate lists. Print the message My favorite pizzas are:
# and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.

print(f"\nMy favourite pizzas are:")
for pizza in favourite_pizzas:
    print(pizza)

print(f"\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
