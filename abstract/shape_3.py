# Level 3: Constructors & Variables - Question 3 (Shape)
# Create an abstract class Shape with a constructor that accepts a color. Add an abstract method area().
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

class ColoredCircle(Shape):
    def __init__(self, color, r):
        super().__init__(color)
        self.r = r
    def area(self):
        return 3.14*self.r*self.r
 