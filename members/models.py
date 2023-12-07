from django.db import models
from datetime import datetime
# Create your models here.

class Employee(models.Model):

    employee_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    joined_date = models.DateField(default=datetime.now, null=True)
    city = models.CharField(max_length=255, default='null')
    department = models.CharField(max_length=255, default='null')


    def __str__(self):
        return f"{self.firstname} {self.lastname}"