# Level 2: Multiple Methods - Question 2 (Shape)
# Create an abstract class Shape with abstract methods area() and perimeter(). Implement them in Rectangle and Circle.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w; self.h=h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
    def perimeter(self):
        return 2*3.14*self.r
