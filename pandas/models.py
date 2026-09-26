"""Simple Django model examples from the assignment.

Copy these models into the models.py file of a Django app.
"""

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    admission_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "assignment_examples"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    is_working = models.BooleanField(default=True)

    class Meta:
        app_label = "assignment_examples"


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "assignment_examples"


class Course(models.Model):
    ONLINE = "online"
    OFFLINE = "offline"
    MODE_CHOICES = [
        (ONLINE, "Online"),
        (OFFLINE, "Offline"),
    ]

    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    trainer_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    start_date = models.DateField()
    number_of_seats = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = "assignment_examples"
