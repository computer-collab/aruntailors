from django.http import *
from django.shortcuts import render
from flask import render_template
from django.template import loader
from flask import session
def root(request):
    return HttpResponse("Hello worl, thinnava")


dictionary = {}
def x(request):
    return render(request, "success.html")

def login(request):
    dictionary["login"] = "login"
    return HttpResponseRedirect("home")

def HomePage(request):
    if not dictionary:
        return HttpResponseRedirect("login")
    else:
        if dictionary:
            return HttpResponse("THIs is the home page")