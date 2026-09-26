# Q2: Create a method that calls another method.
class Person:
    def say_name(self):
        return "Asha"

    def introduce(self):
        print("My name is", self.say_name())

Person().introduce()
