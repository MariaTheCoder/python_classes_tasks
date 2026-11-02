# Opgave:
#
# Her er en ny datafil animal_counts_large.csv med en hel masse tællinger af dyr fra dyreparken.
#
# Lav et færdigt bar-chart-plot af disse data som de står i filen (altså lad først programmet læse filen)
# – husk overskrift, farver og akse-titler.

import csv
import matplotlib.pyplot as plt

animals = []
counts = []

with open("animal_counts_large.csv", newline="") as f:
    reader = csv.reader(f)

    # skip den første linje
    next(reader)

    for animal, count in reader:
        animals.append(animal)
        counts.append(int(count))

total_count = sum(counts)

plt.bar(animals, counts, color="teal")

plt.title("Distribution of animals")
plt.xlabel("Animal")
plt.ylabel("Count")
plt.xticks(range(len(animals)), animals, rotation=90)
plt.tight_layout()

plt.show()
