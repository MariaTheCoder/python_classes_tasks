# Opgave 3-9.
#
# Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42),
# use len() to print a message indicating the number of people you’re inviting to dinner.

dinner_guests = ["Aunt Anna", "Uncle Henrik", "Kirsten"]

print(f"Hi {dinner_guests[0]}! You are invited for dinner next Friday. Bring your best mood. See you then!")
print(f"Greetings {dinner_guests[1]}! You are invited for dinner next Friday. Bring your best mood. See you then!")
print(f"Hello {dinner_guests[2]}! You are invited for dinner next Friday. Bring your best mood. See you then!")

# Uncle Henrik cannot make it!
print(f"\nHello User. It's {dinner_guests[1]}. I can't make it but I hope the rest of you have lots of fun!")

# That is very unfortunate. So let us remove Uncle Henrik from the guest list and invite mom instead.
dinner_guests[1] = "Mom"

# Check whether the original guest list has been modified
print(f"\nHere is our new, modified guest list: {dinner_guests}")

# How long is the list?
print("\nHow many guests are currently on the guest list?", len(dinner_guests))


# Opgave 3-10.

# Every Function: Think of things you could store in a list. For example, you could make a list of mountains,
# rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list
# containing these items and then uses each function introduced in this chapter at least once

hobbies = ["bicycling", "reading", "gaming"]
favourite_hobbies = []

if len(hobbies) > 0:
    for hobby in hobbies:
        if hobby == "bicycling":
            favourite_hobbies.append(hobby)

favourite_hobbies[len(favourite_hobbies)] = "netflix"
favourite_hobbies[len(favourite_hobbies)] = "cooking"

print("Updated list of favourite hobbies:", favourite_hobbies)