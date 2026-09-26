"""Python OOP relationships workbook: IS-A, HAS-A, and USES-A examples."""


# Level 1: IS-A means one class inherits from another class.

class Vehicle:
    def move(self):
        return "The vehicle moves"


class Car(Vehicle):
    def move(self):
        return "The car drives"


class Bike(Vehicle):
    def move(self):
        return "The bike rides"


class Bus(Vehicle):
    def move(self):
        return "The bus carries people"


class Animal:
    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    pass


class Developer(Employee):
    pass


class Tester(Employee):
    pass


class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance


class CurrentAccount:
    def __init__(self, balance):
        self.balance = balance


# Level 2: HAS-A means an object keeps or owns another object.

class Engine:
    def start(self):
        return "Engine started"


class CarWithEngine:
    def __init__(self):
        self.engine = Engine()


class CPU:
    def process(self):
        return "CPU is working"


class Computer:
    def __init__(self, cpu):
        self.cpu = cpu


class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self, rooms):
        self.rooms = rooms


class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self, books):
        self.books = books


class College:
    def __init__(self, students):
        self.students = students


class Department:
    def __init__(self, employees):
        self.employees = employees


class School:
    def __init__(self, teachers, students):
        self.teachers = teachers
        self.students = students


class Company:
    def __init__(self, departments, employees):
        self.departments = departments
        self.employees = employees


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def total(self):
        return sum(product.price for product in self.products)


class Hospital:
    def __init__(self, doctors, patients):
        self.doctors = doctors
        self.patients = patients


# Level 3: USES-A means a method uses a helper object to do a job.

class Printer:
    def print_text(self, text):
        print(text)


class PaymentService:
    def pay(self, amount):
        return "Paid " + str(amount)


class SearchService:
    def find(self, items, word):
        return [item for item in items if word.lower() in item.lower()]


class NotificationService:
    def send(self, message):
        return "Message sent: " + message


class BillingService:
    def make_bill(self, amount):
        return "Bill: " + str(amount)


class StudentUsesPrinter(Student):
    def print_details(self, printer):
        printer.print_text(self.name + " " + self.student_id)


class AccountUsesPayment:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, service, amount):
        if amount > self.balance:
            return "Not enough money"
        self.balance -= amount
        return service.pay(amount)


class CartUsesGateway(ShoppingCart):
    def checkout(self, gateway):
        return gateway.pay(self.total())


class LibraryUsesSearch(Library):
    def search(self, service, title):
        titles = [book.title for book in self.books]
        return service.find(titles, title)


class HospitalUsesBilling(Hospital):
    def bill_patient(self, service, amount):
        return service.make_bill(amount)


# Level 4: These labels show the relationship in each short scenario.

RELATIONSHIP_ANSWERS = {
    "Dog and Animal": "IS-A",
    "Car and Engine": "HAS-A",
    "Student and Printer": "USES-A",
    "Manager and Employee": "IS-A",
    "Library and Books": "HAS-A",
    "ShoppingCart and PaymentGateway": "USES-A",
    "Laptop and Keyboard": "HAS-A",
    "Teacher and Person": "IS-A",
    "Order and PaymentService": "USES-A",
    "Company and Employees": "HAS-A",
}


# Level 5: Combined relationships.

class Course:
    def __init__(self, name):
        self.name = name


class StudentWithCourse(Student):
    def __init__(self, name, student_id, course):
        super().__init__(name, student_id)
        self.course = course


class Laptop:
    def __init__(self, model):
        self.model = model


class DeveloperWithLaptop(Developer):
    def __init__(self, name, salary, laptop):
        super().__init__(name, salary)
        self.laptop = laptop


class OnlineOrder:
    def __init__(self, products):
        self.products = products

    def total(self):
        return sum(product.price for product in self.products)

    def checkout(self, payment_service):
        return payment_service.pay(self.total())


class EducationalInstitution:
    def __init__(self, name):
        self.name = name


class University(EducationalInstitution):
    def __init__(self, name, departments):
        super().__init__(name)
        self.departments = departments

    def hold_exam(self, exam_service):
        return exam_service.run_exam(self.name)


class ExaminationService:
    def run_exam(self, university_name):
        return "Exam started at " + university_name


def main():
    print("Dog sound:", Dog().sound())
    print("Car action:", Car().move())

    car = CarWithEngine()
    print(car.engine.start())
    cart = CartUsesGateway([Product("Book", 8), Product("Pen", 2)])
    print("Cart total:", cart.total())
    print(cart.checkout(PaymentService()))

    student = StudentWithCourse("Ava", "S1", Course("Python"))
    print(student.name, "takes", student.course.name)
    university = University("North College", [Department([])])
    print(university.hold_exam(ExaminationService()))
    print("Scenario answers:", RELATIONSHIP_ANSWERS)


if __name__ == "__main__":
    main()
