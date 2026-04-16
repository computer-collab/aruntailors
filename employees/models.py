from django.db import models
from django.db.models import *

# Create your models here.

class Employees(models.Model):
    pass

# # class CreateEmployees(models.Model):
# #     Name = CharField(max_length=1000)
# #     Username = CharField(max_length=1000, unique=True, primary_key=True)
# #     Password = CharField(null= False)
# #     class EmployeeProfile(models.Model):
# #         Employee = ForeignKey(CreateEmployees, on_delete=CASCADE)
# #         ProfilePicture = ImageField(upload_to='profile_pictures/', null=True, blank=True)
# #         Bio = TextField(null=True, blank=True)
# #         Email = EmailField(null=True, blank=True)
# #         PhoneNumber = CharField(max_length=20, null=True, blank=True)
# #         PerUnitSalary = IntegerField(null=True, blank=True)
# #         TotalUnits = IntegerField(null=True, blank=True)
# #         TotalSalary = IntegerField(null=True, blank=True)

#     def __init__(self,**args):
#         self.Name = args.get('name')
#         self.Username = args.get('username')
#         self.Password = args.get('password')
#         self.EmployeeProfile = self.EmployeeProfile(
#             Employee=self,
#             ProfilePicture=args.get('profile_picture'),
#             Bio=args.get('bio'),
#             Email=args.get('email'),
#             PhoneNumber=args.get('phone_number'),
#             PerUnitSalary=args.get('per_unit_salary'),
#             TotalUnits=args.get('total_units'),
#             TotalSalary=args.get('total_salary')
#         )


#     def SaveProfilePicture(self, profile_picture):
#         self.EmployeeProfile.ProfilePicture = profile_picture
#         profile_picture_name = self.Username + '_profile_picture.jpg'
#         self.EmployeeProfile.ProfilePicture.name = profile_picture_name
#         self.EmployeeProfile.save()
#     def login(self, username, password):
#         User = CreateEmployees.objects.filter(Username = username )
#         if User.Username == username and User.Password == password:
#             return True
#         else:
#             return False
