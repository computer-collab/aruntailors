from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


username_validator = RegexValidator(
    regex=r'^[A-Za-z0-9_]+$',
    message='Username can contain only letters and underscores'
)


class Profile(models.Model):
    Admin = models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile")
    Bio = models.TextField(blank=True)
    DateOfBirth = models.DateField(null=True, blank=True)
    PhoneNumber = models.CharField(max_length=15)
    Address = models.CharField(max_length=1000, null = True, blank= False)
    

