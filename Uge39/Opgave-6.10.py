# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favourite_numbers = {'alice': [3, 5, 10], 'benny': [10], 'charlie': 7, 'daniel': [13, 3], 'ellen': [7]}

for person, numbers in favourite_numbers.items():

    # first, let's check if numbers is of data type list or int

    if type(numbers) is int:
        print(f"{person.title()}'s favorite numbers is {numbers}.")


    elif type(numbers) is list:

        # check if the list contains only one value
        # if it does, print out that one number in its own line
        if len(numbers) == 1:
            print(f"{person.title()}'s favorite numbers is {numbers[0]}.")

        # if it contains more than one number, loop through the list and print each number
        # in its own line
        else:
            for number in numbers:
                print(f"One of {person.title()}'s favorite numbers is {number}.")
