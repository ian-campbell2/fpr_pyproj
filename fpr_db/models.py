from django.db import models
from django.contrib.auth.models import User


#grade choices for the parent to select from on the new_student form
grade_choices = ['1','2','3','4','5','6','7','8','9','10','11','12']

# Create your models here

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


class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)


class Camp(models.Model):
    name = models.CharField(max_length=40)
    #student = models.ForeignKey(Student, on_delete=models...)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    description = models.CharField(max_length=2000, null=True)
    cost = models.FloatField(default='0.00')
    
class Student(models.Model):
    #camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=15, null=True)
    zipcode = models.CharField(max_length=5, null=True)
    bday = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=2, default='n/a')
    comment = models.CharField(max_length=150, default='n/a')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=2)


class CampRegistration(models.Model):
    transaction_date = models.DateField(auto_now=True, auto_now_add=False)
    payment_received = models.CharField(max_length=1)   # Y or N
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE,null=True)
    notes = models.CharField(max_length=150, default='n/a')


