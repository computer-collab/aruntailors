from django.shortcuts import render,redirect
from django.http import request,JsonResponse,HttpResponse,HttpResponseRedirect
import json
import modules
from django.contrib.auth import login, logout, decorators,authenticate, models
from django.contrib import sessions



def AdminDashboard(request):
    if request.method  == "GET":
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request,"admin/admin_dashboard.html")
           
        else:
            return HttpResponseRedirect("login")

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

def AdminForgotDetails(request):
    if request.method == "GET":
        return render(request,"admin/admin_forgot_details.html")
    
    elif request.method == "POST":
        details_pack = json.loads(request.body)
        request_type = details_pack.get("request_type").lower()
        if request_type == "generate_otp":
            request_email = details_pack.get("email")
            modules.GenerateOTP(request_email,"forgot_details")
            return JsonResponse({"message" : "hi"})
        
    
def AdminLogout(request):
    logout(request)
    return HttpResponse("Logout successful")