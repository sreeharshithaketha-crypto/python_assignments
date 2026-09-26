# Level 2: Multiple Methods - Question 8 (Delivery)
# Create an abstract class Delivery with abstract methods calculate_charge() and deliver(). Implement them using StandardDelivery and ExpressDelivery.
from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

class StandardDelivery(Delivery):
    def calculate_charge(self):
        return 5
    def deliver(self):
        return "standard delivered"

class ExpressDelivery(Delivery):
    def calculate_charge(self):
        return 15
    def deliver(self):
        return "express delivered"
