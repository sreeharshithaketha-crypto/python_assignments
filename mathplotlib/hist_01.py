import matplotlib.pyplot as plt

x = [35, 42, 45, 48, 51, 55, 58, 61, 65, 67, 72, 75, 78, 81, 85, 88, 91, 95]

plt.hist(x, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(axis="y")
plt.show()
