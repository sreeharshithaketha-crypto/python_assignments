# Q7: Create three Laptop objects.
class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

laptops = [Laptop("Dell", "8GB", "512GB", 55000), Laptop("HP", "16GB", "1TB", 70000), Laptop("Lenovo", "8GB", "256GB", 45000)]
for laptop in laptops:
    print(laptop.brand, laptop.ram, laptop.storage, laptop.price)
