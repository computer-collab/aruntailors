from django.shortcuts import render
from django.http import request,JsonResponse,HttpResponse
import json
import modules
from django.contrib.auth import login, logout, decorators,authenticate, models


def AdminDashboard(request):
    if request.method  == "GET":
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request,"admin/admin_dashboard.html")
           
        else:
            return JsonResponse({"message" : "Please login"})

def AdminLogin(request):
    if request.method == "GET":
        return render(request,"admin/admin_login.html")
    
    elif request.method == "POST":
        login_pack = json.loads(request.body)
        Username = login_pack.get("username")
        Password = login_pack.get("password")
        user = authenticate(request,username=Username,password=Password)
        if user is not None:
            login (request,user)
            return JsonResponse ({ "message" : login_pack.get("username"), "status":"ok" })
        else :
            return JsonResponse({ "message" : "request failed"})
        
def AdminRegister(request): 
    pass

def ForgotPassword(request):
    if request.method == "GET":
        return render(request,"admin/ForgotPassword.html")
    
def AdminLogout(request):
    logout(request)
    return HttpResponse("Logout successful")