# Opgave 5-8.

print(f"\nOpgave 5-8.")

# Hello Admin: Make a list of five or more usernames, including the name 'admin'.
usernames = ["maria", "markus", "jackie", "rasmus", "admin"]

# Imagine you are writing code that will print a greeting to each user after they log in to a website.
# Loop through the list, and print a greeting to each user.

# * If the username is 'admin', print a special greeting, such as Hello admin,would you like to see a status report?
# * Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

for username in usernames:
    if username == "admin":
        print(f"Hello {username}! Would you like to see a status report?")
    else :
        print(f"Hello {username.title()}, thank you for logging in again.")

# Opgave 5-9.

print(f"\nOpgave 5-9.")

# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#
# If the list is empty, print the message We need to find some users!
# Remove all usernames from your list, and make sure the correct message is printed.

usernames = []

if len(usernames) == 0:
    print("We need to find some users!")

else:
    print("We do have users!")
    for username in usernames:
        if username == "admin":
            print(f"Hello {username}! Would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")

# Opgave 5-10.

print(f"\nOpgave 5-10.")

# Checking Usernames: Do the following to create a program that simulates how websites
# ensure that everyone has a unique username.

# * Make a list of five or more usernames called current_users.
current_users = ["Maria", "Markus", "Kewin", "Tommy", "Klaus"]

# * Make another list of five usernames called new_users. Make sure one or two of the new
# usernames are also in the current_users list.
new_users = ["jackie", "dennis", "rasmus", "maria", "tommy"]

# * Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying that the username is available.
# * Make sure your comparison is case-insensitive. If 'John' has been used, 'JOHN' should not be accepted.
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

copy_current_users = []

for current_user in current_users:
    copy_current_users.append(current_user.lower())

print("copy_current_users:", copy_current_users)

index = 0

for index in range(len(copy_current_users)):
    for user in new_users:
        if user.lower() == copy_current_users[index]:
            print(f"username '{user}' is already in use.")