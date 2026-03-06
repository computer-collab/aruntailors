from employees.views import rod
from django.urls import path
from admin import views
from admin.views import test
# from django.http import request

urlpatterns = [
    path("login",views.AdminLogin),
    path("register",views.AdminRegister),
    path("forgot_password", views.ForgotPassword),
    path("test",test)
]