import matplotlib.pyplot as plt

# Exercise 6: Make a 2-by-2 dashboard with four different charts.
# Answer: The four charts show the same monthly sales in different ways.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 115, 140, 160, 155]
month_numbers = [1, 2, 3, 4, 5, 6]

fig, axes = plt.subplots(2, 2, figsize=(9, 6))

axes[0, 0].plot(months, sales, marker="o")
axes[0, 0].set_title("Line Chart")

axes[0, 1].bar(months, sales)
axes[0, 1].set_title("Bar Chart")

axes[1, 0].hist(sales, bins=4, edgecolor="black")
axes[1, 0].set_title("Sales Histogram")

axes[1, 1].scatter(month_numbers, sales)
axes[1, 1].set_title("Sales Scatter Plot")
axes[1, 1].set_xlabel("Month Number")
axes[1, 1].set_ylabel("Sales")

plt.tight_layout()
plt.show()
