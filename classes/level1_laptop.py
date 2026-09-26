# Q6: Create a Laptop object with its specifications.
class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

laptop = Laptop("Dell", "8 GB", "i5", 55000)
print(laptop.brand, laptop.ram, laptop.processor, laptop.price)
