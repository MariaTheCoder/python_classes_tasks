# Opgave: Brugere og aldre med statistik
# I denne opgave skal løse disse underopgaver:
# Først laves en liste med 8 fornavne på personer (gemt som strings)
# first_names = ["klaus", "kewin", "markus", "maria", "jackie", "nicklas", "rasmus", "dennis"]

# Nu skal I lave en ny tom liste (der senere skal indeholde tal).
# I denne liste skal brugernes alder, (indtastes fra tastaturet) placeres (Husk at konvertere tekst til int).
# ages = []

# for first_name in first_names:
#    age = int(input(f"How old is {first_name.title()}? "))
#    ages.append(age)

# print(ages)

# Programmet skal nu udregne gennemsnittet af brugernes alder.
# average = sum(ages) / len(ages)
# print(f"The average age is: {average}")

# Til slut skal udskrives en oversigt over brugere og aldre (brug print-f) samt gennemsnittet.
# index = 0

# for count in range(len(first_names)):
#    print(f"{first_names[index]} is {ages[index]} years old.")
#    index += 1


# Opgave: Fejlslagne ”login-attempts” på én server hver dag i en uge
# Lav først en liste med navnene på de 7 ugedage, derefter:
# I en loop: indlæs antallet af ”attempts” for hver dag i ugen (fra tastaturet). Bemærk hver indlæst
# værdi skal over i en ny liste som tal, hvilket jo kræver konvertering.
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
daily_attempts = []

for weekday in weekdays:
    attempts = int(input(f"How many failed attempts at logging in occurred on {weekday}? "))
    daily_attempts.append(attempts)

print("\nDaily attempts:", daily_attempts)

# Programmet nu lave en del beregninger: summen af alle attempts i hele ugen. Gennemsnittet af attempts pr. dag.
sum = 0

for attempts in daily_attempts:
    sum += attempts

print(f"\nSum: {sum}")
print(f"\nAverage: {round(sum/len(daily_attempts),2)}")

#
# Svær:20
# I skal også finde (og udskrive) den ugedag hvor der var færrest og den ugedag hvor der var flest
# attempts (hint: man loope igennem hele listen og gemme det hidtil største mindste antal login-
# forsøg. Man kan også prøve at bruge indbygget funktion kaldet min() hhv max. Udfordringen er
# stadig at finde (og udskrive) ugedagen hvor det sker J

attempts_min = daily_attempts[0]
attempts_max = daily_attempts[0]

for attempt in daily_attempts:
    if attempt > attempts_max:
        attempts_max = attempt

print("\nMax attempts this week is: ", attempts_max)

for attempt in daily_attempts:
    if attempt < attempts_min:
        attempts_min = attempt

print("Min attempts this weeks is:", attempts_min)

# Alternatively, you can use a simpler method to find min and max value.
print("\nMAX value:", max(daily_attempts))
print("MIN value:", min(daily_attempts))

# Til slut skal der udprintes oversigter hvor man kan se dag-for-dag hvad der er sket + de udregnede
# statistiske værdier. Her kan I bruge print-f-kommandoen.
print("\n-- OVERVIEW --")
for count in range(len(daily_attempts)):
    print(f"Login attempts on {weekdays[count]}: {daily_attempts[count]}")