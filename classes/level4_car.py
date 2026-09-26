# Q7: Create Car start, stop, and display_details methods.
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def display_details(self):
        print(self.brand)

car = Car("Toyota")
car.start()
car.display_details()
car.stop()
