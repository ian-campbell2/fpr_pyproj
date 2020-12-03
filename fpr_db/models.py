from django.db import models

# Create your models here.

class Parent(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)

class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
#this ia a test to see if i can go to my branch
class Camp(models.Model):
    name = models.CharField(max_length=40)
    #student = models.ForeignKey(Student, on_delete=models...)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

class Student(models.Model):
    #camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    

class Registration(models.Model):
    transaction_date = models.DateField(auto_now=True, auto_now_add=True)
    payment_received = models.CharField(max_length=1)   # Y or N
    notes = models.CharField(max_length=150)