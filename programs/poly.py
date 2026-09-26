#1
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

c = Calculator()
print("Addition of 2 numbers:", c.add(10, 20))
print("Addition of 3 numbers:", c.add(10, 20, 30))

#2
class area:
    def calculate(self, l=None, br=None, pie=None, r=None):
        if l is not None and br is not None:
            print("Area of rectangle is: ", l * br)
        elif pie is not None and r is not None:
            print("Area of circle is: ", pie * (r * r))
        else:
            print("Area of square is: ", (l * l))
a = area()
a.calculate(5, 10)
a.calculate(5,5, 3.14, 5)
a.calculate(5)

#3
class Display:
    def show(self,a=None,b=None,c=None):
        if a is not None:
            print(a)
        if b is not None:
            print(b)
        if c is not None:
            print(c)
d=Display()
d.show("Python")
d.show("python","java")
d.show("python","java","c")

#4
class student:
    def stu(self, name=None, age=None, roll=None):
        print("Name:", name)
        print("Age:", age)
        print("Roll:", roll)
s = student()
s.stu("John", 20, 101)
s.stu("Alice", 22)
s.stu("Bob")

#5
class Employee:
    def salary(self, salary, bonus=0):
        totalsalary = salary + bonus
        print("Total Salary: ", totalsalary)
sal = Employee()
sal.salary(50000)
sal.salary(50000, 5000)

#6 
class Message:
    def display(self, *args):
        if len(args) == 1:
            print("Welcome, ", args[0], "!")
        elif len(args) == 2:
            print("Welcome, ", args[0], " and ", args[1], "!")
        else:
            print("Welcome all!")
m = Message()
m.display("yashu")
m.display("yashu", "manu")
m.display("anu", "yashu", "manu")

#7
class Bank:
    def deposit(self, amount, amount2=0, amount3=0):
        if amount2 == 0 and amount3 == 0:
            print("Depositing amount: ", amount)
        else:
            print("Depositing amount: ", amount)
            if amount2 != 0:
                print("Additional deposit: ", amount2)
            if amount3 != 0:
                print("Additional deposit: ", amount3)
b = Bank()
b.deposit(1000)
b.deposit(1000, 500, 250)

#8
class MathOperations:
    def multiply(self, a, b, c=1):
        return a * b * c

m = MathOperations()
print(m.multiply(5, 5))
print(m.multiply(5, 5, 5))

#9
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price, quantity=1):
        self.items.append((item, price, quantity))

    def calculate_total(self):
        total = 0
        for _, price, quantity in self.items:
            total += price * quantity
        return total

cart = ShoppingCart()
cart.add_item("Apple", 10, 5)
cart.add_item("Banana", 3, 10)
print("Total price: ", cart.calculate_total())

#10
class TemperatureConverter:
    def convert(self,celsius,unit):
        if unit=="F":
            print("Farenheit:",(celsius * 9/5)+32)
        elif unit=="K":
            print("Kelvin:",celsius +273)
t= TemperatureConverter()
t.convert(25,"F")
t.convert(25,"K")

#Create a Vehicle class and override the start() method in Car, Bike, and Bus classes.
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting...")

class Bus(Vehicle):
    def start(self):
        print("Bus is starting...")
c = Car()
c.start()
b = Bike()
b.start()
bus = Bus()
bus.start()

#Write a Python program where an Animal class has a sound() method and override it in Dog, Cat, and Cow classes to produce different sounds.
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

class Cow(Animal):
    def sound(self):
        print("Cow moos")
d = Dog()
d.sound()
c = Cat()
c.sound()
cow = Cow()
cow.sound()

#Create an Employee class and override the calculate_salary() method in Managerand Developer.
class Employee:
    def calsalary(self):
        print("Calculating salary for employee")
class Manager(Employee):
    def calsalary(self):
        print("Calculating salary for manager")
class Developer(Employee):
    def calsalary(self):
        print("Calculating salary for developer")
m = Manager()
m.calsalary()
d = Developer()
d.calsalary()

#Write a program to demonstrate method overriding using Person and Teacher classes.
class Person:
    def introduce(self):
        print("I am a person.")

class Teacher(Person):
    def introduce(self):
        print("I am a teacher.")

t = Teacher()
t.introduce()

#Create a Shape class with an area() method and override it in Rectangle, Circle, and triangle 
class Shape:
    def area(self):
        print("Calculating area of shapes")
class Rectangle(Shape):
    def area(self, length, breadth):
        print("Area of rectangle: ", length * breadth)

class Circle(Shape):
    def area(self, radius, pie=3.14):
        print("Area of circle: ", pie * radius * radius)

class Triangle(Shape):
    def area(self, base, height):
        print("Area of triangle: ", 0.5 * base * height)
        
r = Rectangle()
r.area(5, 10)
c = Circle()
c.area(5)
t = Triangle()
t.area(5, 10)

#Write a Python program to override the withdraw() method in a SavingsAccount classinherited from BankAccount.
class BankAccount:
    def withdraw(self, amount):
        print("Withdrawing amount: ", amount)

class Savings(BankAccount):
    def withdraw(self, amount):
        print("Withdrawing amount from savings account: ", amount)
bank = BankAccount()
bank.withdraw(1000)
savings = Savings()
savings.withdraw(1000)

#Create a Payment class and override the pay() method in CreditCardPayment,UPIPayment, and CashPayment.
class Payment:
    def pay(self, amount):
        print("Paying amount: ", amount)

class CreditCard(Payment):
    def pay(self, amount):
        print("Paying with credit card: ", amount)

class UPI(Payment):
    def pay(self, amount):
        print("Paying with UPI: ", amount)

class Cash(Payment):
    def pay(self, amount):
        print("Paying with cash: ", amount)
cc = CreditCard()
cc.pay(1000)
upi = UPI()
upi.pay(1000)
cash = Cash()
cash.pay(1000)

#Write a program to override the display() method in a Student class inherited by GraduateStudent.
class Student:
    def display(self):
        print("Displaying student information")
class GraduateStudent(Student):
    def display(self):
        print("Displaying graduate student information")

s = Student()
s.display()
g = GraduateStudent()
g.display()

#Create a Bird class with a fly() method and override it in Sparrow, Eagle, and Penguin.
class Bird:
    def fly(self):
        print("Flying in the sky")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Eagle(Bird):
    def fly(self):
        print("Eagle flying")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

sp = Sparrow()
e = Eagle()
p = Penguin()

sp.fly()
e.fly()
p.fly()

#Write a Python program to demonstrate method overriding using Hospital and SpecializedHospital classes.
class Hospital:
    def patient(self):
        print("patient in general hospital")

class Specialized(Hospital):
    def patient(self):
        print("patient in specialized hospital")
h = Hospital()
sh = Specialized()
h.patient()
sh.patient()

# Create two classes  Duck  and  Person  where both have a  talk()  method. Demonstrate duck typing.

class Duck:
    def talk(self):
        print("Quack!")

class Person:
    def talk(self):
        print("Hello!")

def ducktyping(obj):
    obj.talk()
    
d = Duck()
p = Person()
ducktyping(d)
ducktyping(p)
#  Create  Dog  and  RobotDog  classes with the same  bark()  method and use duck typing. 

class Dog:
    def bark(self):
        print("Woof!")
        
class Robot:
    def bark(self):
        print("Beep! Beep!")
        
def ducktyping(obj):
    obj.bark()

dog = Dog()
robot = Robot()

ducktyping(dog)
ducktyping(robot)


#  Write a program where  Teacher  and  YouTubeInstructor  both implement a  teach() method
class Teacher:
    def teach(self):
        print("Teaching in a classroom.")

class YouTubeInstructor:
    def teach(self):
        print("Teaching on YouTube.")
        
def ducktyping(obj):
    obj.teach()

# Test the classes
t = Teacher()
y = YouTubeInstructor()

ducktyping(t)
ducktyping(y)
#  Create  EmailNotification  and  SMSNotification  classes  with the same  send() method.
class EmailNotification:
    def send(self):
        print("Sending email notification.")

class SMSNotification:
    def send(self):
        print("Sending SMS notification.")

def ducktyping(obj):
    obj.send()

# Test the classes
email = EmailNotification()
sms = SMSNotification()

ducktyping(email)
ducktyping(sms)
#  Write a program using  Car  and  Bike  classes that  both implement a  start()  method. 
class Car:
    def start(self):
        print("Car is starting with engine.")
        
class Bike:
    def start(self):
        print("Bike is starting with kick.")
        
def ducktyping(obj):
    obj.start()
    
# Test the classes
car = Car()
bike = Bike()
ducktyping(car)
ducktyping(bike)


# Create  PDFFile  and  WordFile  classes that both  implement an  open()  method. 
class PDFFile:
    def open(self):
        print("Opening PDF file.")

class WordFile:
    def open(self):
        print("Opening Word file.")

def ducktyping(obj):
    obj.open()

# Test the classes
pdf = PDFFile()
word = WordFile()

ducktyping(pdf)
ducktyping(word)
#.  Write a program where  Student  and  Employee  classes  both implement an  introduce() method. 
class Student:
    def introduce(self):
        print("I am a student.")
        
class Employee:
    def introduce(self):
        print("I am an employee.")
        
def ducktyping(obj):
    obj.introduce()

# Test the classes
student = Student()
employee = Employee()

ducktyping(student)
ducktyping(employee)
# Create  Laptop  and  Desktop  classes with the same  power_on()  method and 
#demonstrate ducktyping
class Laptop:
    def power_on(self):
        print("Laptop is powering on.")

class Desktop:
    def power_on(self):
        print("Desktop is powering on.")

def ducktyping(obj):
    obj.power_on()

# Test the classes
laptop = Laptop()
desktop = Desktop()

ducktyping(laptop)
ducktyping(desktop)

#Write a program where  OnlinePayment  ,  CardPayment  ,  and  CashPayment  all implement process_payment()  method.
class OnlinePayment:
    def process_payment(self):
        print("Processing online payment.")
        
class CardPayment:
    def process_payment(self):
        print("Processing card payment.")
        
class CashPayment:
    def process_payment(self):
        print("Processing cash payment.")

def ducktyping(obj):
    obj.process_payment()

# Test the classes
online = OnlinePayment()
card = CardPayment()
cash = CashPayment()

ducktyping(online)
ducktyping(card)
ducktyping(cash)

#  Create three classes  Lion  ,  Dog  , and  Baby  where  each has a  sound()  method. Write a function that accepts any object and calls the  sound()  method without checking its type
class Lion:
    def sound(self):
        print("Roar!")
        
class Dog:
    def sound(self):
        print("Woof!")
        
class Baby:
    def sound(self):
        print("Cry!")
        
def ducktyping(obj):
    obj.sound()

# Test the classes
lion = Lion()
dog = Dog()
baby = Baby()

ducktyping(lion)
ducktyping(dog)
ducktyping(baby)