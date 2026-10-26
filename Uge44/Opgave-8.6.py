# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values
# that are returned.

def city_country(city, country):
    return f'\n{city.title()}, {country.title()}'


response_one = city_country("Wuppertal", "Germany")
response_two = city_country("Bramming", "Denmark")
response_three = city_country("London", "England")

print(response_one, response_two, response_three)
