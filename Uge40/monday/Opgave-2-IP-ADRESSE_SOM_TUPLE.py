# OPGAVE 2 – IP-ADRESSE SOM TUPLE
# En IPv4-adresse består af fire tal.
# Opret IP-adressen 192.168.1.25 som en tuple:
# ip = (192, 168, 1, 25)
# Udskriv hele tuplen.
# Udskriv kun det første tal.
# Udskriv kun det sidste tal.
# Brug et for-loop til at udskrive alle fire tal.
# Prøv til sidst:
# ip[3] = 30 Hvad sker der? Forklar hvorfor.

ip = (192, 168, 1, 25)

print("hele tuplen:", ip)

print(ip[0])

print(ip[len(ip) - 1])

for num in ip:
    print(num)

# Vi kan ikke overskrive enkelte vårdier inde i en tuplet. En tuplet er immutable