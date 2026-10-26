# 6-6. Polling: Use the code in favorite_languages.py (page 96).

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.

best_friends = ["anna", "carlo", "edward", "jenny", "jen", "phil"]

# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

for friend in best_friends:
    if friend in favorite_languages.keys():
        print(f"Thank you for responding, {friend.title()}!")
    else:
        print(f"Hello {friend.title()}, feel free to take the poll.")
