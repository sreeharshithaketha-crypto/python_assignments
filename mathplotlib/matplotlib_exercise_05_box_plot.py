import matplotlib.pyplot as plt

# Exercise 5: Make a salary box plot and look for unusual values.
# Answer: No salary looks like an outlier in this small sample.
salary = [25000, 28000, 32000, 38000, 43000, 50000, 58000]

plt.boxplot(salary)
plt.title("Salary Box Plot")
plt.ylabel("Salary")
plt.show()
