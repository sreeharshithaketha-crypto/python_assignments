# Q6: Calculate product total price using __init__.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

product = Product("Pen", 10, 5)
print(product.name, product.total_price())
