cities = ["Esbjerg", "Odense", "Aarhus"]

# vi laver en ny variable som er en kopi af cities
# metoden hernede svarer til my_cities = cities.copy()
my_cities = cities[:]

# undgå at gøre dette!!!!
# my_cities = cities

# tilføj et nyt element til den nye copi
cities.append("Varde")

# vis at disse to lister ikke indeholder det samme
print("cities:", cities)
print("my_cities:", my_cities)

# Tupler kan ikke ændres
location = (55.4765, 8.4594)

# location kan ikke ændres
# location[0] = 57.5643

# Overskrid værdien af variablen
location = (57.5643, 8.4594)
