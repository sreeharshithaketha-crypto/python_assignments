# Q9: Add products, remove products, and calculate cart total.
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add(self, name, price):
        self.products.append([name, price])

    def remove(self, name):
        self.products = [product for product in self.products if product[0] != name]

    def total(self):
        return sum(product[1] for product in self.products)

cart = ShoppingCart()
cart.add("Pen", 10)
cart.add("Book", 50)
cart.remove("Pen")
print(cart.total())
