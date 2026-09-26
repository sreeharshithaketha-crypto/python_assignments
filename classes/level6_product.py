# Q5: Accept quantity and return the product total price.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity

print(Product("Pen", 10).total_price(5))
