import matplotlib.pyplot as plt
import pandas as pd

# Exercise 5: Make a DataFrame and compare age and salary histograms.
# Answer: Ages are more tightly grouped; both charts have a right tail.
# Answer: The salary chart is more strongly right-skewed because of $120,000.
employees = pd.DataFrame({
    "Age": [22, 24, 25, 26, 27, 28, 29, 30, 32, 35, 42, 58],
    "Salary": [30000, 32000, 35000, 36000, 38000, 40000,
               42000, 45000, 48000, 50000, 55000, 120000],
})

plt.hist(employees["Age"], bins=5, edgecolor="black")
plt.title("Employee Ages")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.show()

plt.hist(employees["Salary"], bins=5, edgecolor="black")
plt.title("Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()
