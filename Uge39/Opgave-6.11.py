# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all the
# information you have stored about it.

cities = {'bramming': {'country': 'denmark', 'population': 7244, 'fact': 'maria is from there!'},
          'wuppertal': {'country': 'germany', 'population': 354382, 'fact': 'kerim is from there!'},
          'prague': {'country': 'czech republic', 'population': 1407084,
                     'fact': 'maria and kerim went there together!'}}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {str(city_info['country']).title()}")
    print(f"Population: {int(city_info['population']):,d} people")
    print(f"Fact: {str(city_info['fact']).title()}")
