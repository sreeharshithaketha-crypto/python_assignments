# Q3: Use a class variable number_of_wheels with different cars.
class Car:
    number_of_wheels = 4

    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")
print(car1.brand, car1.number_of_wheels)
print(car2.brand, car2.number_of_wheels)
