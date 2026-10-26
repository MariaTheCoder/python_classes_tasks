# Opgave 3-8.

# Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.

countries = ["greece", "turkey", "panama", "fiji", "norway"]

# Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.

print("original countries list: ", countries)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
print("\ncountries before sorting:", countries)
print("sorted(countries):", sorted(countries))
print("countries after sorting:", countries)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
print("\ncountries before sorting:", countries)
print("sorted(countries, reverse=True):", sorted(countries, reverse=True))
print("countries after sorting:", countries)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
print("\ncountries before countries.reverse():", countries)
countries.reverse()
print("countries after countries.reverse():", countries)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print("\ncountries before countries.reverse():", countries)
countries.reverse()
print("countries after countries.reverse():", countries)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print("\ncountries before countries.sort():", countries)
countries.sort()
print("countries after countries.sort():", countries)

# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.
print("\ncountries before countries.sort(reverse=True):", countries)
countries.sort(reverse=True)
print("countries after countries.sort(reverse=True):", countries)

