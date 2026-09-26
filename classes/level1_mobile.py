# Q4: Create a Mobile class with brand, model, and price.
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

mobile = Mobile("Samsung", "A15", 18000)
print(mobile.brand, mobile.model, mobile.price)
