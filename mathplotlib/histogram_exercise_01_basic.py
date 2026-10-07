import matplotlib.pyplot as plt

# Exercise 1: Plot the marks with a title, labels, and a grid.
# Answer: The histogram groups marks into ranges and counts them.
marks = [35, 42, 45, 48, 51, 55, 58, 61, 65, 67, 72, 75, 78, 81, 85, 88, 91, 95]

plt.hist(marks, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(axis="y")
plt.show()
