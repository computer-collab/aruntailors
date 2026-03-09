from django.contrib import admin
from django.urls import path,include
from employees.views import rod
from myadmin import urls
from aruntailors import views as aruntailors
urlpatterns = [
    path("admin/",include(urls)),
    path("", aruntailors.Home)
    
]
