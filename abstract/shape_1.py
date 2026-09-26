# Level 1: Basic Abstract Classes - Question 3 (Shape)
# Create an abstract class Shape with an abstract method area(). Implement it in Circle and Rectangle.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w; self.h = h
    def area(self):
        return self.w * self.h

if __name__ == "__main__":
    print(Circle(2).area())
    print(Rectangle(2,3).area())
