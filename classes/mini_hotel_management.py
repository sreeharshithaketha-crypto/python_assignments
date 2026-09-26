# Mini Project 9: Simple hotel management system.
class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.booked = False

class Customer:
    def __init__(self, name):
        self.name = name

class Booking:
    def __init__(self, customer, room):
        self.customer = customer
        self.room = room
        room.booked = True

booking = Booking(Customer("Asha"), Room(101, 2000))
print(booking.customer.name, booking.room.number, booking.room.price)
