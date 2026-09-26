# Q6: Count the total number of objects created.
class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

user1 = User("A")
user2 = User("B")
user3 = User("C")
print("Objects:", User.count)
