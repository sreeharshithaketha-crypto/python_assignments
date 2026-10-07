import matplotlib.pyplot as plt

# Exercise 3: Plot salaries with 5 bins and answer the salary questions.
# Answer: The $22,000-$41,600 range has the most people (11).
# Answer: The salaries are not symmetric; the chart is right-skewed.
# Answer: $120,000 is unusually high compared with most salaries.
# Answer: Yes, a box plot can help us look for unusual salaries.
salary = [
    22000, 25000, 27000, 28000, 30000,
    31000, 32000, 35000, 36000, 38000,
    40000, 42000, 45000, 47000, 50000,
    52000, 55000, 60000, 75000, 120000,
]

plt.hist(salary, bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()
