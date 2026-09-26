# Level 3: Constructors & Variables - Question 5 (Product)
# Create an abstract class Product with product name and price. Add an abstract method calculate_discount().
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

class SimpleProduct(Product):
    def calculate_discount(self):
        return self.price * 0.1
