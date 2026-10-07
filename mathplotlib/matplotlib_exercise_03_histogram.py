import matplotlib.pyplot as plt

# Exercise 3: Compare the marks histogram using 4, 6, and 10 bins.
# Answer: Fewer bins make a simpler chart. More bins show more detail.
marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 90]
bin_counts = [4, 6, 10]

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for ax, bin_count in zip(axes, bin_counts):
    ax.hist(marks, bins=bin_count, edgecolor="black")
    ax.set_title(str(bin_count) + " bins")
    ax.set_xlabel("Marks")
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.show()
