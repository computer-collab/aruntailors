from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile")
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    