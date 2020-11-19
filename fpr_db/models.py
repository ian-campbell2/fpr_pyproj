from django.db import models

# Create your models here.
'''
class Parent(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
'''

class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    #camp = models.ForeignKey(Camp, on_delete=models...)


class Camp(models.Model):
    name = models.CharField(max_length=40)
    #student = models.ForeignKey(Student, on_delete=models...)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


