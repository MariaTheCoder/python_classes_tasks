import matplotlib.pyplot as plt
import numpy as np

# Indsæt vores data som vi skal plotte i grafen senere, rå data i lister
temperature = [15, 17, 16, 18, 20, 19, 21, 23, 22, 24, 26, 25, 27, 29, 28]
ice_cream_sales = [30, 38, 35, 45, 55, 52, 60, 72, 68, 80, 95, 90, 100, 115, 110]

# Valg data til henholdsvis første- og andenaksen i vores scatter diagram
plt.scatter(temperature, ice_cream_sales)

a, b = np.polyfit(temperature, ice_cream_sales, 1)
# Hvad mon 1-tallet betyder?
# Betyder at vi undersøger for en linjear sammenhæng, altså x opløftet i 1

plt.scatter(temperature, ice_cream_sales)

# Vis lineær progressions-linje og tilknyt et label til en grafisk navngivning af linjen
plt.plot(temperature, [a*t + b for t in temperature], label="Fitted line")

# Husk plot.legend() ellers vises vores nye label ikke på grafen
plt.legend()

# Formatér graf
plt.title("Salg af is"), plt.xlabel("temperatur (grader Celsius)"), plt.ylabel("salg af is (stk.)")

# Udskriv vores graf så vi kan se den
plt.show()