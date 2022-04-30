from tkinter import CASCADE
from django.db import models

class Departments(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=500)

class Employees(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    dateOfJoining = models.DateField()
    photoFileName = models.CharField(max_length=500)