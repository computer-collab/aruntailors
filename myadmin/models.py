from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


username_validator = RegexValidator(
    regex=r'^[A-Za-z0-9_]+$',
    message='Username can contain only letters and underscores'
)


class Profile(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile")
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    

