# Opgave Modulus og input fra tastaturet

# Eksempel: Vi laver denne lille algoritme fælles

# Vi beder brugeren om at indtaste et (stort) helt tal
# Programmet skriver så tilbage om det indtastede tal var lige eller ulige
# (det må jo nok være en af delene )

number = int(input("Type in a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")