# Opgave 5.3
print("\nOpgave 5.3")

alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")

# Let us try again but this time we chance the value of the variable alien_color
alien_color = "red"

if alien_color == "green":
    print("The player just earned 5 points.")

# Opgave 5.4
print("\nOpgave 5.4")

# Alien Colors number 2: Choose a color for an alien as you did in Exercise 5-3,and write an if-else chain.

# * If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# * If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# * Write one version of this program that runs the if block and another that runs the else block.

if alien_color == "green":
    print("The player just earned 5 points.")
elif alien_color != "green":
    print("The player just earned 10 points.")

# Does the code still work as intended if we change the value of the alien_color valuable

alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points.")
elif alien_color != "green":
    print("The player just earned 10 points.")

# Opgave 5-5.
print("\nOpgave 5.5")
# Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#
# * If the alien is green, print a message that the player earned 5 points.
# * If the alien is yellow, print a message that the player earned 10 points.
# * If the alien is red, print a message that the player earned 15 points.
# * Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color = "yellow"

if alien_color == "green":
    print("You have earned 5 points.")
elif alien_color == "yellow":
    print("You have earned 10 points.")
else:
    print("You have earned 15 points.")

# Opgave 5-6.
print("\nOpgave 5.6")
# Stages of Life: Write an if-elif-else chain that determines a person’s stage of life.
# Set a value for the variable age, and then:
age = 18

# * If the person is less than 2 years old, print a message that the person is a baby.
# * If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# * If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# * If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# * If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# * If the person is age 65 or older, print a message that the person is an elder.

if age > 2:
    print("The person is a baby!")