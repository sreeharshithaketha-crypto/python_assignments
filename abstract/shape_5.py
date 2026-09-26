# Level 5: Abstract + Concrete Methods - Question 3 (Shape)
# Create an abstract Shape class with an abstract method area() and a normal method display_shape().
from abc import ABC, abstractmethod

class Shape(ABC):
    def display_shape(self):
        return "shape"

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a*self.a
