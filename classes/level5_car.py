# Q4: Use __init__ with start, stop, and display methods.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def display(self):
        print(self.brand, self.model)

car = Car("Honda", "City")
car.start()
car.display()
car.stop()
