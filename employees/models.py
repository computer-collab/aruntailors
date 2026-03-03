from django.db import models
from django.db.models import *

# Create your models here.

class Employees(models.Model):
    pass

class CreateEmployees(models.Model):
    Name = CharField(max_length=1000)
    Username = CharField(max_length=1000, unique=True, primary_key=True)
    Password = CharField(null= False)
    def login(self, username, password):
        User = CreateEmployees.objects.filter(Username = username )
        if User.Username == username and User.Password == password:
            return True
        else:
            return False
