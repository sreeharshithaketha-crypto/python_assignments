import matplotlib.pyplot as plt

# Exercise 1: Make a line chart with markers, labels, a grid, and a legend.
# Answer: Sales are highest in May and go down a little in June.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 115, 140, 160, 155]

plt.plot(months, sales, marker="o", label="Sales")
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.show()
