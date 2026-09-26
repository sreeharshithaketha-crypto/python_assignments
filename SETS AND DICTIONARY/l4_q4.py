# 4. Create a dictionary containing product names and quantities. Display products with quantity less than 10.
products = {"pens": 5, "books": 12, "bags": 7}
for product, quantity in products.items():
    if quantity < 10:
        print(product)
