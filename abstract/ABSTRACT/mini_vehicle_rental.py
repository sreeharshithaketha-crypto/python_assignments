# Mini Project 4: Vehicle Rental System
# Build a Vehicle Rental System using an abstract Vehicle class and different vehicle types.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def rent(self):
        pass

class Car(Vehicle):
    def rent(self):
        return "car rent"
