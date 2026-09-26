# Level 5: Abstract + Concrete Methods - Question 5 (Payment)
# Create an abstract Payment class with an abstract method pay() and a normal method display_amount().
from abc import ABC, abstractmethod

class Payment(ABC):
    def display_amount(self):
        return "amount"

    @abstractmethod
    def pay(self):
        pass

class Card(Payment):
    def pay(self):
        return "card pay"
