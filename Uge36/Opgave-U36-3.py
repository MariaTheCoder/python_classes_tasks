# Opgave 3

# Lav din egen lille beregner

# Programmet skal spørge efter to tal.
print("Hej! Jeg vil gerne bede dig om at give mig to tal. Vi tager lige et tal af gangen.")
print("Jeg gider kun positive heltal.")

first_num = input("Okay, vælg dit første tal: ")
second_num = input("Og dit andet tal: ")

# Lad os gøre vores liv lettere for os selv og konvertere de to tal til integers med det samme
first_num = int(first_num)
second_num = int(second_num)

# Derefter skal det vise:

#  summen
res = first_num + second_num
print("\nSummen af de to tal bliver da", res)

#  forskellen
diff = first_num-second_num
print("Forskellen mellem to to tal er", abs(diff))

#  produktet (når tallene ganges)
product = first_num * second_num
print("Produktet mellem de to tal er", product)