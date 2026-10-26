while True:
    number = input("Enter a number from 1 to 10: ")

    if number.isdigit(): # check data type
        number = int(number)

        if 1 <= number <= 10:
            break
    print("Invalid input - try again")

print('complete')