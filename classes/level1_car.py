# Q2: Create a Car class and three objects with different values.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")
car3 = Car("Ford", "White")
print(car1.brand, car1.color)
print(car2.brand, car2.color)
print(car3.brand, car3.color)
