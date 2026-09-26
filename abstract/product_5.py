# Level 5: Abstract + Concrete Methods - Question 7 (Product)
# Create an abstract Product class with an abstract method calculate_discount() and a normal method display_product().
from abc import ABC, abstractmethod

class Product(ABC):
    def display_product(self):
        return "product"

    @abstractmethod
    def calculate_discount(self):
        pass

class Item(Product):
    def __init__(self,price):
        self.price=price
    def calculate_discount(self):
        return self.price*0.1
