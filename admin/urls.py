from employees.views import rod
from django.urls import path
from admin import views

# from django.http import request

urlpatterns = [
    path("dashboard",views.AdminDashboard),
    path("login",views.AdminLogin),
    path("logout",views.AdminLogout),
    path("forgot_details",views.AdminForgotDetails)
]