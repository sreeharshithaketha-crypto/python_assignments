# Level 2: Multiple Methods - Question 1 (Vehicle)
# Create an abstract class Vehicle with abstract methods start() and stop(). Implement both methods in Car and Bike.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "car start"
    def stop(self):
        return "car stop"

class Bike(Vehicle):
    def start(self):
        return "bike start"
    def stop(self):
        return "bike stop"
