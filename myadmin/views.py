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
        request_type = details_pack.get("request_type")
        if request_type == "setup" :
            return JsonResponse({ "setup" : request.session.get("setup" , "none") })
        
        if request_type == "generate_otp":
            request_email = details_pack.get("email")
            request.session["setup"] = "email_done"
            request.session["email"] = request_email
            request.session.set_expiry(3600)
            server_otp = modules.GenerateOTP(email=request_email,request=request_type)
            request.session["otp"] = server_otp
            return JsonResponse({"status" : "ok", "message" :"Email Has been sent." })
        
        elif request_type == "verify_email":
            request_otp = details_pack.get("otp")
            if request.session["otp"] and request_otp == request.session.get("otp"):
                request.session["setup"] = "otp_done"
                request.session.pop
                return JsonResponse({ "message" : "Your Otp has been verified" , "status" : "ok"})
        
    
def AdminLogout(request):
    logout(request)
    return HttpResponse("Logout successful")



def x(request):
    return HttpResponseRedirect(request,"dashboard")