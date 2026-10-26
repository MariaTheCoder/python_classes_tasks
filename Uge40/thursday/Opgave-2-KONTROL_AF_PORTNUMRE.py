# OPGAVE 2 – KONTROL AF PORTNUMRE
# Et portnummer i TCP/IP kan være mellem 1 og 65535.
# Lav et program, som gentagne gange spørger brugeren:
# Enter port number or quit:
# Programmet skal stoppe, når brugeren skriver:
# quit
# Kontrollér først, om input er et tal.
# Hvis det ikke er et tal, udskrives:
# Invalid input
# Hvis det er et tal, skal det konverteres til int.
# Kontrollér derefter, om tallet ligger mellem 1 og 65535.
# Hvis det ikke gør, udskrives:
# Invalid port number
# Opret denne tuple:
# common_ports = (22, 80, 443)
# Hvis det indtastede portnummer findes i common_ports, skal programmet skrive:
# Common port
# Ellers skal programmet skrive:
# Other valid port
# Eksempel:
# Enter port number or quit: 443
# Common port
# Enter port number or quit: 8080
# Other valid port
# Enter port number or quit: hello
# Invalid input
# Enter port number or quit: 70000
# Invalid port number
# Enter port number or quit: quit
# Program stopped
# Du får brug for:
# while
# input()
# isdigit()
# int()
# if / elif / else
# in
# tuple
# break

common_ports = (22, 80, 443)

while True:
    port = input("Enter port number or quit: ")

    if port == "quit":
        break

    if port.isdigit():
        port = int(port)

        if 1 <= port <= 65535:
            if port in common_ports:
                print("Common port.")
            else:
                print("Other valid port.")

        else:
            print("Invalid port number")

    else:
        print("Invalid input")
