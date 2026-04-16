from employees.views import rod
from django.urls import path
from myadmin import views

# from django.http import request

urlpatterns = [
    path("", views.AdminRoot),
    path("dashboard",views.AdminDashboard),
    path("login",views.AdminLogin),
    path("logout",views.AdminLogout),
    path("forgot_details",views.AdminForgotDetails),
    path("profiles/pics/<picname>",views.profile_pic)

]
