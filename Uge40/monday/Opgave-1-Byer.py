# Opgave 1 Byer
# Lav en liste med mindst 8 forskellige byer.
# Brug slices til at udskrive:
# De første tre byer
# De sidste tre byer
# Tre byer fra midten
# Lav derefter et loop som kun gennemløber de første fire byer.
# Udskriv: I would like to visit Esbjerg
# for hver af de fire byer. (Det med gult skal jo skiftes ud for hver by)

cities = ["esbjerg", "bramming", "aarhus", "sønderborg", "gørding", "viby j", "odder", "varde"]

# udskriv de første tre byer
print(cities[:3])

# udskriv de sidste tre byer
print(cities[-3:])

# udskriv de midterste tre byer
print(cities[3:6])

# loop fire første byer
for city in cities[:4]:
    print(f"I would like to visit {city.title()}")
