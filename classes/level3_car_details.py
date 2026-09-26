# Q9: Use class variables company and number_of_wheels with car details.
class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

car = Car("Camry", 2500000)
print(car.company, car.number_of_wheels, car.model, car.price)
