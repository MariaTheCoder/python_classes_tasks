# Opgave (den gemmes til slut i dag)

# Dyre-park observationerne skal ind i en tabel,
# Men først skal læses de fra en fil
# Udfordring: hvordan få man header-teksten ind i tabellen (fra første linje) og så derefter tællingerne?

import csv
import plotly.graph_objects as go


header = []
animals = []
counts = []

with open("animal_counts_large.csv", newline="") as f:
    reader = csv.reader(f)

    animal_label, count_label = next(reader)
    header.append(animal_label)
    header.append(count_label)

    for animal, count in reader:
        animals.append(animal)
        counts.append(int(count))

print(header)
print(animals)
print(counts)

fig = go.Figure(data=[go.Table(
    header=dict(values=header),
    cells=dict(values=[animals, counts])
)])

fig.show()