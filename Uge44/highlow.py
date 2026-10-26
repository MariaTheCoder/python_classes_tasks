import random


def think_of_random_number():
    """
    Think of a random number between 1 and 100

    Parameter
    No parameters

    Return
    Returns a random integer between 1 and 100
    """
    return random.randint(1, 100)


def guess_number():
    """
    Ask the user for a random number between 1 and 100

    Parameter
    No parameters

    Return
    Returns the user's guess as an integer between 1 and 100
    """
    user_guess = int(input("\nGuess a number between 1 and 100: "))
    return user_guess


def compare(r_num, g_num):
    """
    Ask the user for a random number between 1 and 100

    Parameter
    Two numbers of type integer

    Return
    An integer between -1 and 1
    Zero meaning that the guess is correct
    Plus one meaning that the user's guess was too low
    Minus one meaning that the user's guess was too high
    """
    if r_num > g_num:
        print("Your guess is too low")
        return 1
    elif r_num < g_num:
        print("Your guess is too high")
        return -1
    else:
        print("You guessed the correct number!")
        return 0


def game():
    guess_count = 0

    computer_number = think_of_random_number()

    while True:
        guessed_number = guess_number()

        comparison = compare(computer_number, guessed_number)

        if comparison == 0:
            print(f"You guessed {guess_count} times!")

            if guess_count > 10:
                print("You guessed more than 10 times. You can do better than that!")
            else:
                print("You are a great guesser!")

            break

        guess_count += 1


game()
