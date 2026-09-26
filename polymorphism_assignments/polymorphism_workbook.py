"""Python Polymorphism workbook: shared method names, overriding, and operators."""

from abc import ABC, abstractmethod
import math


# Level 1-2: Different classes can have the same method name.

class Animal:
    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Cow(Animal):
    def sound(self):
        return "Moo"


class Vehicle:
    def start(self):
        return "Vehicle started"


class Car(Vehicle):
    def start(self):
        return "Car started"


class Bike(Vehicle):
    def start(self):
        return "Bike started"


class Bus(Vehicle):
    def start(self):
        return "Bus started"


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class EmailNotification:
    def send(self):
        return "Email sent"


class SMSNotification:
    def send(self):
        return "SMS sent"


class UPIPayment:
    def pay(self, amount):
        return "Paid by UPI: " + str(amount)


class CardPayment:
    def pay(self, amount):
        return "Paid by card: " + str(amount)


class CashPayment:
    def pay(self, amount):
        return "Paid with cash: " + str(amount)


def make_sound(animal):
    print(animal.sound())


def start_vehicle(vehicle):
    print(vehicle.start())


def send_notification(notification):
    print(notification.send())


def process_payment(payment, amount):
    print(payment.pay(amount))


# Level 3-4: Duck typing uses the method an object has.

class Duck:
    def walk(self):
        return "Duck walks"


class WalkingDog:
    def walk(self):
        return "Dog walks"


def take_a_walk(thing):
    return thing.walk()


class PDFReport:
    def generate(self):
        return "PDF report created"


class ExcelReport:
    def generate(self):
        return "Excel report created"


def generate_report(report):
    return report.generate()


# Level 5: Operator overloading lets objects use familiar operators.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)


class RectangleBox:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __eq__(self, other):
        return self.area() == other.area()


class ShoppingCart:
    def __init__(self, products=None):
        self.products = products or []

    def __add__(self, other):
        return ShoppingCart(self.products + other.products)

    def total(self):
        return sum(self.products)


# Level 6: Abstract classes require child classes to implement methods.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class RectangleShape(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class AbstractUPI(Payment):
    def pay(self, amount):
        return "UPI paid " + str(amount)


class AbstractCard(Payment):
    def pay(self, amount):
        return "Card paid " + str(amount)


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(Notification):
    def send(self, message):
        return "Email: " + message


class TextMessage(Notification):
    def send(self, message):
        return "Text: " + message


def show_areas(shapes):
    for shape in shapes:
        print("Area:", shape.area())


# Mini-project style examples: same operation, different implementation.

def checkout(payment_method, total):
    return payment_method.pay(total)


def open_file(file_object):
    return file_object.read()


class TextFile:
    def __init__(self, text):
        self.text = text

    def read(self):
        return self.text


class WordFile(TextFile):
    pass


class CSVFile(TextFile):
    pass


def main():
    make_sound(Dog())
    make_sound(Cat())
    start_vehicle(Car())
    send_notification(EmailNotification())
    process_payment(UPIPayment(), 25)

    print(take_a_walk(Duck()))
    print(take_a_walk(WalkingDog()))
    print(generate_report(PDFReport()))

    print(Point(2, 3) + Point(4, 1))
    print("Book one is pricier:", Book("A", 20) > Book("B", 10))
    print("Student one scored higher:", Student("Ava", 90) > Student("Ben", 80))
    print("Money total:", (Money(5) + Money(7)).amount)
    print("Same rectangle area:", RectangleBox(2, 6) == RectangleBox(3, 4))

    show_areas([CircleShape(2), RectangleShape(3, 4)])
    print(checkout(AbstractCard(), 30))
    print(open_file(CSVFile("name,marks")))


if __name__ == "__main__":
    main()
