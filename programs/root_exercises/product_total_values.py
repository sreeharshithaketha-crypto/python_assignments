# 2. Create a list of tuples containing product name, price, and quantity. Calculate the total value of each product.
products = [("Pen", 10, 3), ("Book", 50, 2), ("Bag", 500, 1)]
for name, price, quantity in products:
    total = price * quantity
    print(name, total)
