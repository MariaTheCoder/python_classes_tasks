# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:

toppings = []

print("Welcome! Make a pizza with three toppings.")

while True:
    # Ask the user for a topping
    topping = input("\nChoose a toping. Type 'quit' to exit. ")

    # In case the user decides to quit, break the loop
    # • Use a break statement to exit the loop when the user enters a 'quit' value.
    if topping == "quit":
        break

    # • Use a conditional test in the while statement to stop the loop.
    if topping == "cheese":
        print("Sorry, we are out of cheese.")
        break

    # In case the user did not decide to quit, display the chosen topic to the user
    toppings.append(topping)
    print(f"You have chosen {topping} as topping.")

    # • Use an active variable to control how long the loop runs.
    if len(toppings) >= 3:
        break

print("\nYou have chosen the following three topings:")
for topping in toppings:
    print(topping)
