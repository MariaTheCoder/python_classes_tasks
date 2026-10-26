# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program, or improving the formatting of the output.

# =====================================================================================

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

people = []

person_1 = {'id': 0, 'first_name': 'jens', 'last_name': 'andersen', 'city': 'bramming'}
person_2 = {'id': 1, 'first_name': 'bjarne', 'last_name': 'winther', 'city': 'tjæreborg'}
person_3 = {'id': 2, 'first_name': 'jesper', 'last_name': 'andersen', 'city': 'gørding', 'parent_id': 0}

people.append(person_1)
people.append(person_2)
people.append(person_3)

for person in people:
    print("Person:\n", person)

    parent_id = person.get('parent_id', None)

    # if we find a person with a living parent (key parent_id appears in dictionary), find parent in list
    if parent_id is not None:
        parent_first_name = ''

        # find parent in list
        for possible_parent in people:
            if possible_parent['id'] == parent_id:
                parent_first_name = possible_parent.get('first_name', None)

        print(
            f"\n{person['first_name'].title()} is the child of {parent_first_name.title()}.")
