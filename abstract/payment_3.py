# Question 3: Payment
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass

class SimpleUPI(Payment):
    def pay(self):
        return f"paid {self.amount} via UPI"
