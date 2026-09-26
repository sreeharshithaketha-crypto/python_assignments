# Q4: Create three Car objects with different values.
class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

cars = [Car("Toyota", "Etios", 2020, 600000), Car("Honda", "City", 2022, 900000), Car("Ford", "Figo", 2019, 500000)]
for car in cars:
    print(car.brand, car.model, car.year, car.price)
