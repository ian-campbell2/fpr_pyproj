from django.db import models

#grade choices for the parent to select from on the new_student form
grade_choices = ['1','2','3','4','5','6','7','8','9','10','11','12']

# Create your models here

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
    bday = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=2)
    comment = models.CharField(max_length=150)

class Registration(models.Model):
    transaction_date = models.DateField(auto_now=True, auto_now_add=False)
    payment_received = models.CharField(max_length=1)   # Y or N
    notes = models.CharField(max_length=150)
