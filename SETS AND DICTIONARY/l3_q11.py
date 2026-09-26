# 11. Create a dictionary of 5 products and their prices. Print all products whose price is greater than Rs. 1,000.
products = {"phone": 15000, "pen": 20, "bag": 1200, "book": 500, "watch": 2500}
for product, price in products.items():
    if price > 1000:
        print(product)
