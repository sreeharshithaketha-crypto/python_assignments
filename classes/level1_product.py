# Q8: Create a Product object and display its information.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product = Product("Pen", 10, 5)
print(product.name, product.price, product.quantity)
