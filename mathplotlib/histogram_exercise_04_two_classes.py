import matplotlib.pyplot as plt

# Exercise 4: Plot both classes and compare their marks.
# Answer: Class B usually has higher marks than Class A.
# Answer: Class A has a mean of about 67.1; Class B has a mean of about 73.2.
class_a = [55, 60, 62, 65, 67, 70, 72, 75, 78]
class_b = [60, 65, 68, 70, 73, 76, 80, 82, 85]

plt.hist(
    [class_a, class_b],
    bins=5,
    alpha=0.6,
    label=["Class A", "Class B"],
    edgecolor="black",
)
plt.title("Marks in Two Classes")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()
plt.show()
