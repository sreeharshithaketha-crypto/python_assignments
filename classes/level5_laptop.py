# Q9: Display complete laptop specifications.
class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

    def display(self):
        print(self.brand, self.ram, self.processor, self.price)

Laptop("Dell", "8GB", "i5", 55000).display()
