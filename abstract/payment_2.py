# Level 2: Multiple Methods - Question 4 (Payment)
# Create an abstract class Payment with abstract methods pay() and refund(). Implement them in UPI, CreditCard, and NetBanking.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class UPI(Payment):
    def pay(self):
        return "upi pay"
    def refund(self):
        return "upi refund"

class CreditCard(Payment):
    def pay(self):
        return "card pay"
    def refund(self):
        return "card refund"

class NetBanking(Payment):
    def pay(self):
        return "netbanking pay"
    def refund(self):
        return "netbanking refund"
