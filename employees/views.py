from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from os import getcwd

print(__file__,"   " , getcwd())
# Create your views here.
def rod (request):
    return HttpResponseRedirect("/")