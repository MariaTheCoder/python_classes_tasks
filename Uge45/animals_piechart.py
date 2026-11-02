# Sidste opgave i dag:
#
# Dyreparken – vis fordelingen af dyr som et lagkage-diagram, I skal læse fra filen
# som før og så lave en beregning (sammentælling af alle dyr + sammentælling + beregne
# frekvensen af de enkelte typer dyr ud fra totalen)

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

pie_data = [count / total_count * 100 for count in counts]

plt.pie(pie_data, labels=animals)
plt.title("Distribution of animals")
plt.show()