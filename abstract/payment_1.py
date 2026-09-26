# Level 1: Basic Abstract Classes - Question 5 (Payment)
# Create an abstract class Payment with an abstract method pay(). Implement it in UPIPayment and CardPayment.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPIPayment(Payment):
    def pay(self):
        return "paid via UPI"

class CardPayment(Payment):
    def pay(self):
        return "paid via Card"

if __name__ == "__main__":
    print(UPIPayment().pay())
    print(CardPayment().pay())
