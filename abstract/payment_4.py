# Level 4: Polymorphism - Question 2 (Payment)
# Create an abstract Payment class and use polymorphism to process different payment methods.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

class UPI(Payment):
    def process(self):
        return "upi processed"

class Card(Payment):
    def process(self):
        return "card processed"
