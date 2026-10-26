# Opgaver i Cyber Programmering – string funktioner

# Opgave A
# Gem følgende log-linje i en variabel og udskriv den:
# 2026-01-01 10:15:23 LOGIN_FAILED user=admin ip=192.168.1.45
logline = "2026-01-01 10:15:23 LOGIN_FAILED user=admin ip=192.168.1.45"

# Opgave B
# Udskriv hvor mange tegn log-linjen fra opgave A indeholder ved hjælp af len().
print(f"\nThe logline string has the following length: {len(logline)}.")

# Opgave C
# Udskriv log-linjen fra opgave A med kun store bogstaver.
print("\nall upper case:", logline.upper())

# Opgave D
# Udskriv log-linjen fra opgave A med kun små bogstaver.
print("\nall lower case:", logline.lower())

# Opgave E
# Lad brugeren indtaste en log-linje og udskriv både log-linjen og dens længde.
new_logline = input("Type in logline:")
print("\nnew logline:", new_logline, "\nLength of new logline:", len(new_logline))

# Opgave F
# Lad brugeren indtaste et brugernavn og udskriv brugernavnet to gange lige efter: den ene gang
# kun med store bogstaver, den anden gang kun med små bogstaver.
username = input("Type in username:")
print(username.upper(), username.lower())

# Opgave G
# Lad brugeren indtaste en IP-adresse som tekst og udskriv hvor mange tegn den indeholder.
ip_address = input("Type in ip address:")
print(f"The typed in IP-address contains this many digits: {len(ip_address)}")

# Opgave H
# Lad brugeren indtaste tre log-linjer og gem dem i tre variabler. Udskriv dem alle igen.
new_logline_one = input("Type in logline one:")
new_logline_two = input("Type in logline two:")
new_logline_three = input("Type in logline three:")

print(f"\nFirst logline provided by the user is: {new_logline_one}.")
print(f"\nSecond logline provided by the user is: {new_logline_two}.")
print(f"\nThird logline provided by the user is: {new_logline_three}.")

# Opgave I
# Udskriv de første 10 tegn af log-linjen fra opgave A (hvilken information giver det os?).
print("Print the first 10 digits:", logline[0:9])

# Opgave J
# Udskriv de sidste 12 tegn af log-linjen fra opgave A (hvilken information giver det os?).
print("Print the last 12 digits:", logline[-12:0])

# Opgave K
# Lad brugeren indtaste en log-linje og udskriv de første 5 tegn (antag at disse tegn giver nyttig info).
new_logline_four = input("Type in new logline:")
print(new_logline_four[0:5])

# Opgave L
# Lad brugeren indtaste en log-linje og udskriv både starten (første 8 tegn) og slutningen (sidste 8
# tegn) i samme linje.
new_logline_five = input("Type in new logline:")
print(f"The first 8 characters: {new_logline_five[0:8]}.\n The last 8 characters: {new_logline_five[-8:]}.")