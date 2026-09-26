# Level 4: Polymorphism - Question 1 (Shape)
# Create an abstract Shape class and use polymorphism to calculate the area of different shapes.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

def area_of(shape: Shape):
    return shape.area()

class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a*self.a

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
