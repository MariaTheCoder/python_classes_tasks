# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

# We want the while loop to run when we run our program
while True:
    # Ask the user for a topping
    topping = input("Choose a toping. Type 'quit' to exit. ")

    # In case the user decides to quit, break the loop
    if topping == "quit":
        break

    # In case the user did not decide to quit, display the chosen topic to the user
    print(f"You have chosen {topping} as topping.")