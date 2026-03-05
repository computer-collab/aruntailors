from employees.views import rod
from django.urls import path
from admin import views
# from django.http import request

urlpatterns = [
    path("login",views.AdminLogin)
]