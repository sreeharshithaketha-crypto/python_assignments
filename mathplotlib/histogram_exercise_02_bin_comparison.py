import matplotlib.pyplot as plt

# Exercise 2: Compare the marks using 3, 5, 10, and 15 bins.
# Answer 1: Three bins group many marks together and hide small differences.
# Answer 2: Fifteen bins show more detail, but the chart can look less smooth.
marks = [35, 42, 45, 48, 51, 55, 58, 61, 65, 67, 72, 75, 78, 81, 85, 88, 91, 95]
bin_counts = [3, 5, 10, 15]

fig, axes = plt.subplots(2, 2, figsize=(9, 6))

for ax, bin_count in zip(axes.flat, bin_counts):
    ax.hist(marks, bins=bin_count, edgecolor="black")
    ax.set_title(str(bin_count) + " bins")
    ax.set_xlabel("Marks")
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.show()
