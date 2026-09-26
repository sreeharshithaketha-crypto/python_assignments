# Q3: Calculate the total price for a Product object.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

product = Product("Bag", 500, 2)
print(product.name, product.total_price())
