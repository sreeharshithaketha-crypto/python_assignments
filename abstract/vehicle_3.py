# Level 3: Constructors & Variables - Question 2 (Vehicle)
# Create an abstract class Vehicle with instance variables brand and model. Add abstract methods start() and stop().
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class SimpleCar(Vehicle):
    def start(self):
        return f"{self.brand} {self.model} started"
    def stop(self):
        return f"{self.brand} {self.model} stopped"
