# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

# • Use a loop to print the name of each river included in the dictionary.
print("\nPrint out rivers:")
for river in rivers.keys():
    print(river.title())

# • Use a loop to print the name of each country included in the dictionary.
print("\nPrint out countries:")
for country in rivers.values():
    print(country.title())
