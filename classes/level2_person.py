# Q5: Create two Person objects and display their information.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person1 = Person("Sam", 20, "Delhi")
person2 = Person("Lia", 22, "Pune")
print(person1.name, person1.age, person1.city)
print(person2.name, person2.age, person2.city)
