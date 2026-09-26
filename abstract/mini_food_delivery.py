# Mini Project 8: Food Delivery System
# Build a Food Delivery System using abstract classes for different delivery methods.
from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Standard(Delivery):
    def deliver(self):
        return "delivered"
