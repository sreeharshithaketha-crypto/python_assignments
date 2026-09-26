# Level 1: Basic Abstract Classes - Question 1 (Animal)
# Create an abstract class Animal with an abstract method sound(). Create Dog and Cat classes that implement sound().
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "woof"

class Cat(Animal):
    def sound(self):
        return "meow"

if __name__ == "__main__":
    print(Dog().sound())
    print(Cat().sound())
