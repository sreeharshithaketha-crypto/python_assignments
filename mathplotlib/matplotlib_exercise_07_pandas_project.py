from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Exercise 7: Read a CSV, chart three number columns, and write three insights.
# Answer 1: Sales are highest in June, at 190.
# Answer 2: Orders are highest in May, at 62.
# Answer 3: More orders usually go with higher sales in this small sample.
data = pd.read_csv(Path(__file__).parent / "sales_data.csv")

plt.plot(data["Month"], data["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.bar(data["Month"], data["Customers"])
plt.title("Customers by Month")
plt.xlabel("Month")
plt.ylabel("Customers")
plt.show()

plt.scatter(data["Orders"], data["Sales"])
plt.title("Orders and Sales")
plt.xlabel("Orders")
plt.ylabel("Sales")
plt.show()
