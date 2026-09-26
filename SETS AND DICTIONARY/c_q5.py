# 5. Create a dictionary of products and prices. Use a set to store all products whose price is above Rs. 5,000.
products = {"phone": 15000, "pen": 20, "laptop": 55000, "bag": 1200}
expensive_products = set()
for product, price in products.items():
    if price > 5000:
        expensive_products.add(product)
print(expensive_products)
