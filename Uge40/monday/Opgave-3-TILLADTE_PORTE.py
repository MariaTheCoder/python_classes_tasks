# OPGAVE 3 – TILLADTE PORTE
# En firewall tillader kun trafik til bestemte porte.
# Gem de tilladte porte i en tuple:
# allowed_ports = (22, 80, 443)
# Lav en variabel:
# port = 443
# Undersøg med if og in, om port findes i allowed_ports.
# Programmet skal udskrive enten:
# Port is allowed
# eller:
# Port is blocked
# Afprøv programmet med:
# 22
# 25
# 80
# 443
# 8080
# Ekstra: Lad brugeren indtaste portnummeret med input().


allowed_ports = (22, 80, 443)

port = 443

if port in allowed_ports:
    print(f"Port {port} is allowed")
else:
    print(f"Port {port} is blocked")

# EKSTRA: Let us try with an input instead

# new_port = int(input("Enter new port (enter quit to stop): "))

# if new_port in allowed_ports:
#     print(f"Port {new_port} is allowed")

# else:
#    print(f"Port {new_port} is blocked")
