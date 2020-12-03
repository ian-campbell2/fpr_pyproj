from django.db import models

# Create your models here.

class Parent(models.Model):
    fname = models.CharField(max_length=50)
    # students
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=15, null=True)
    zipcode = models.CharField(max_length=5, null=True)

class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=14, null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=15, null=True)
    zipcode = models.CharField(max_length=5, null=True)

class Camp(models.Model):
    name = models.CharField(max_length=40)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    description = models.CharField(max_length=2000, null=True)



