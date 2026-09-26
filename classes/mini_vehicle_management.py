# Mini Project 8: Simple vehicle management system.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

vehicles = [Car("Toyota"), Bike("Yamaha"), Truck("Tata")]
for vehicle in vehicles:
    print(vehicle.brand)
