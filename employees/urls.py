from django.urls import path
from employees.views import rod


urlpatterns = [ 
    path("", rod)
]