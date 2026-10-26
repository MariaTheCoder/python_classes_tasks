# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionar-
# ies in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

people = []

person_1 = {'first_name': 'jens', 'last_name': 'andersen', 'city': 'bramming'}
person_2 = {'first_name': 'bjarne', 'last_name': 'winther', 'city': 'tjæreborg'}
person_3 = {'first_name': 'jesper', 'last_name': 'andersen', 'city': 'gørding'}

people.append(person_1)
people.append(person_2)
people.append(person_3)

for person in people:
    print(person)
