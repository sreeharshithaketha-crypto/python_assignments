import matplotlib.pyplot as plt

# Exercise 2: Make a bar chart and find the highest and lowest month.
# Answer: May has the highest sales (160). January has the lowest (100).
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 115, 140, 160, 155]

plt.bar(months, sales)
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
