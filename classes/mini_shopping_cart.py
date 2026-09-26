# Mini Project 5: Simple shopping cart system.
class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append([name, price])

    def remove(self, name):
        self.items = [item for item in self.items if item[0] != name]

    def total(self):
        return sum(item[1] for item in self.items)

cart = Cart()
cart.add("Book", 100)
cart.add("Pen", 10)
cart.remove("Pen")
print(cart.items)
print(cart.total())
