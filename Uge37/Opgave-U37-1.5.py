# Opgave (Udfordring) : (Split en restaurant-regning - Version #2)

# Vi bruger en ny version af et for-loop til huske et varierende antal gæsters navne.
# Først skal brugeren altså indtaste hvor mange gæster der er i alt.
# Og senere skal navnene på gæsterne gemmes (ét navn ad gangen)

# Man kan arbejde med kode der ser sådan ud: (dette loop gennemløbes præcis 5 gange -
# udfordringen er at bruge antallet af gæster til at begrænse loop’et).

# for x in range(1,5):
#    print(x)

# Ask the user how many guests they expect for dinner
number_of_guests = int(input("Number of guests: "))

# Purely for control purposes, print the number of expected guests
print(number_of_guests)

# Create an empty list what will contain the name of our guests
friends = []

# For each guest until we reach the range of the number of guests, so exactly three time, prompt a message to
# user and ask them to type in the name of a guest on their list. The name should then be added to the list of guests
for guest in range(number_of_guests):
    friend = input("Name of friend: ")
    friends.append(friend)

# Once ouf of the loop, print the final list of friends
print("List of guests coming for dinner:", friends)

# for friend in friends:
#    print("One of my friends is named", friend)

# This ends the new addition to previous solution to the split-bil exercise.
# The rest is the same as previously