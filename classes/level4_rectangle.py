# Q4: Create Rectangle methods for area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(10, 5)
print(rectangle.area())
print(rectangle.perimeter())
