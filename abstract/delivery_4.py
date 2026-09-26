# Level 4: Polymorphism - Question 8 (Delivery)
# Create an abstract Delivery class and use polymorphism to calculate different delivery charges.
from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass

class Standard(Delivery):
    def calculate_charge(self):
        return 5

class Express(Delivery):
    def calculate_charge(self):
        return 20
