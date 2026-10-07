import matplotlib.pyplot as plt

# Exercise 8: Make at least five charts and write one insight for each.
# The lesson gives this small example sales dataset. It is not company data.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 130, 180, 210, 190]
orders = [40, 45, 42, 55, 62, 58]

# Chart 1 answer: Sales rise to 210 in May, then fall to 190 in June.
plt.plot(months, sales, marker="o")
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Chart 2 answer: May has the most orders, with 62.
plt.bar(months, orders)
plt.title("Orders by Month")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.show()

# Chart 3 answer: The order counts are between 40 and 62 in this sample.
plt.hist(orders, bins=4, edgecolor="black")
plt.title("Order Counts")
plt.xlabel("Orders")
plt.ylabel("Frequency")
plt.show()

# Chart 4 answer: Months with more orders usually have more sales.
plt.scatter(orders, sales)
plt.title("Orders and Sales")
plt.xlabel("Orders")
plt.ylabel("Sales")
plt.show()

# Chart 5 answer: Sales range from 120 to 210, with a middle value of 165.
plt.boxplot(sales)
plt.title("Sales Box Plot")
plt.ylabel("Sales")
plt.show()
