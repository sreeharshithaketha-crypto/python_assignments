import matplotlib.pyplot as plt

# Exercise 4: Plot experience and salary and say what the chart shows.
# Answer: Salary goes up as experience goes up in this sample.
experience = [1, 2, 3, 4, 5, 6, 7]
salary = [25000, 28000, 32000, 38000, 43000, 50000, 58000]

plt.scatter(experience, salary)
plt.title("Experience and Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
