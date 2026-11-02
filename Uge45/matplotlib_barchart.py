import matplotlib.pyplot as plt

labels = ["A", "B"]
values = [10, 5]

plt.bar(labels, values)

plt.title("Security Events"), plt.xlabel("Event type"), plt.ylabel("Count")

plt.show()
