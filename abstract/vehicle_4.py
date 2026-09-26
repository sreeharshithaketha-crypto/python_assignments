# Level 4: Polymorphism - Question 3 (Vehicle)
# Create an abstract Vehicle class and use polymorphism to start different vehicles.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "car start"

class Bike(Vehicle):
    def start(self):
        return "bike start"
