# Q8: Store products in a cart and calculate the total bill.
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add(self, name, price):
        self.products.append([name, price])

    def total(self):
        return sum(product[1] for product in self.products)

cart = ShoppingCart()
cart.add("Book", 100)
cart.add("Pen", 10)
print(cart.total())
