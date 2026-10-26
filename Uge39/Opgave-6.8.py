# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pets = []

pet_1 = {'name': 'Jakob', 'species': 'canary'}
pet_2 = {'name': 'Trille', 'species': 'canary'}
pet_3 = {'name': 'Bølle', 'species': 'dog'}
pet_4 = {'namee': 'Guffe', 'species': 'guinea pig'}
pet_5 = {'namee': 'Minnie', 'species': 'guinea pig'}

pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)
pets.append(pet_4)
pets.append(pet_5)

for pet in pets:
    print(pet)
