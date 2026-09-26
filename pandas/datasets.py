"""Small Pandas practice tables for IPL, weather, bank, and shopping data."""

import pandas as pd


# IPL: find leading players and compare teams.
ipl = pd.DataFrame({
    "Player": ["Asha", "Bala", "Chin", "Devi", "Esha", "Farah"],
    "Team": ["Tigers", "Tigers", "Waves", "Waves", "Tigers", "Stars"],
    "Runs": [500, 350, 620, 280, 410, 550],
    "Matches": [10, 9, 12, 8, 10, 11],
    "Average": [50.0, 38.9, 51.7, 35.0, 41.0, 50.0],
    "StrikeRate": [140.0, 125.0, 155.0, 110.0, 132.0, 148.0],
})

print("IPL: highest runs")
print(ipl.loc[ipl["Runs"].idxmax()])
print("\nIPL: top five players")
print(ipl.sort_values("Runs", ascending=False).head(5))
print("\nIPL: average runs by team")
print(ipl.groupby("Team")["Runs"].mean())
print("\nIPL: highest strike rate")
print(ipl.loc[ipl["StrikeRate"].idxmax()])
print("\nIPL: runs sorted from low to high")
print(ipl.sort_values("Runs"))


# Weather: compare temperatures and rainfall.
weather = pd.DataFrame({
    "City": ["Rajahmundry", "Hyderabad", "Chennai", "Vijayawada", "Delhi"],
    "Temperature": [34, 39, 36, 41, 32],
    "Humidity": [70, 45, 65, 50, 40],
    "Rainfall": [12, 4, 20, 8, 2],
})

print("\nWeather: average temperature")
print(weather["Temperature"].mean())
print("\nWeather: hottest city")
print(weather.loc[weather["Temperature"].idxmax()])
print("\nWeather: coldest city")
print(weather.loc[weather["Temperature"].idxmin()])
print("\nWeather: cities hotter than 35 degrees")
print(weather[weather["Temperature"] > 35])
print("\nWeather: rainfall from low to high")
print(weather.sort_values("Rainfall"))


# Bank: look at customer balances, loans, and cities.
bank = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104, 105],
    "Name": ["Anu", "Bala", "Chin", "Devi", "Esha"],
    "Balance": [25000, 90000, 50000, 120000, 40000],
    "Loan": [0, 650000, 200000, 800000, 100000],
    "City": ["Hyderabad", "Chennai", "Hyderabad", "Delhi", "Chennai"],
})

print("\nBank: highest balance")
print(bank.loc[bank["Balance"].idxmax()])
print("\nBank: lowest balance")
print(bank.loc[bank["Balance"].idxmin()])
print("\nBank: customers with loans above 500000")
print(bank[bank["Loan"] > 500000])
print("\nBank: customers in each city")
print(bank["City"].value_counts())
print("\nBank: total balance")
print(bank["Balance"].sum())


# Shopping: compare products and calculate inventory value.
shop = pd.DataFrame({
    "Product": ["Book", "Bag", "Pen", "Bottle", "Pencil"],
    "Price": [10, 30, 2, 15, 1],
    "Category": ["School", "School", "School", "Home", "School"],
    "Quantity": [20, 5, 100, 12, 80],
    "Rating": [4.5, 4.8, 4.0, 4.2, 3.9],
})

print("\nShop: most expensive product")
print(shop.loc[shop["Price"].idxmax()])
print("\nShop: cheapest product")
print(shop.loc[shop["Price"].idxmin()])
print("\nShop: average rating")
print(shop["Rating"].mean())
print("\nShop: products in each category")
print(shop["Category"].value_counts())
print("\nShop: total inventory value")
print((shop["Price"] * shop["Quantity"]).sum())
