# Opgaver i Cyber Security: Tal og beregninger.

# I opgaverne nedenfor er det en god idé at gemme værdier i variabler og måske bruge f-strings til output.
# Husk også altid at input() som udgangspunkt er ren tekst så derfor er det nødvendigt at konvertere den
# indtastede værdi enten med int() eller float()

# Opgave A
# Spørg brugeren om hvor mange login-forsøg der blev registreret i system A og i system B og udskriv til slut det
# samlede antal forsøg.
login_attempts_system_A = input("Please enter your login attempts system A: ")
login_attempts_system_B = input("Please enter your login attempts system B: ")
print(f"\nTotal login attempts across both systems: {int(login_attempts_system_A) + int(login_attempts_system_B)}")

# Opgave B
# Spørg brugeren om hvor mange mislykkede login-forsøg der var i går og i dag og udskriv forskellen
# mellem dem (i dag minus i går).
failed_login_attempts_yesterday = input("Please enter your failed login attempts yesterday: ")
failed_login_attempts_today = input("Please enter your failed login attempts today: ")
print(f"\nThe difference is then: {int(failed_login_attempts_yesterday) - int(failed_login_attempts_today)}")

# Opgave C
# Spørg brugeren om hvor mange pakker der blev sendt og hvor mange der blev blokeret af
# firewallen og udskriv produktet af tallene.
packets_sent = input("Please enter packets sent: ")
packets_blocked = input("Please enter packets blocked: ")
print(f"\nProducts of these numbers: {int(packets_sent) * int(packets_blocked)}")

# Opgave D
# Spørg brugeren om den samlede datamængde (MB) og tiden (sekunder) og udskriv den
# gennemsnitlige datahastighed (MB pr sekund).
data_amount = input("Please enter your data amount (in MB): ")
time = input("Please enter your time (in seconds): ")

print(f"\nAverage dataspeed: {float(data_amount)/float(time)} MB/seconds.")

# Opgave E
# Spørg brugeren om antallet af angreb fra én IP-adresse og udskriv tallet opløftet i anden potens
# (dvs. vi simulerer belastning).
attacks = int(input("Please enter attacks from ONE IP-address: "))
print(f"\nSecond power of attacks: {attacks ** 2}")

# Opgave F
# Spørg brugeren om fem målinger af netværkstrafik (i MB) og udskriv gennemsnittet.
l/