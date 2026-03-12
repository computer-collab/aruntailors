from django.shortcuts import render,redirect
from django.http import request,JsonResponse,HttpResponse,HttpResponseRedirect
import json
import modules
from django.contrib.auth import login, logout, decorators,authenticate, models
from django.contrib import sessions
from modules import time
from modules.mails import MaskEmail, GenerateOTP


status = "status" 
message = "message"

def AdminRoot(request):
    return HttpResponseRedirect("dashboard")

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
            return JsonResponse({ "message" : "Invalid Credentials!!"})
        
def AdminRegister(request): 
    pass

def AdminForgotDetails(request):
    
    returnjson = {
        "message" : "",
        "status" : request.session.get("status", "none"),
        }
    if request.method == "GET":
        return render(request,"admin/admin_forgot_details.html")
    
    elif request.method == "POST":
        print(request.session.get("setup", "none"), json.loads(request.body).get("request_type"))
        details_pack = json.loads(request.body)
        request_type = details_pack.get("request_type")
        if request_type == "setup" :
            return JsonResponse({"setup" : request.session.get("setup","none")})
        
        # Step 1 : Generate OTP and send to email
        if request_type == "generate_otp":
            request.session["request"] = details_pack.get("request")
            request_username = details_pack.get("username")
            request.session["setup"] = "username_done"
            request.session["username"] = request_username
            QueryUser = models.User.objects.filter(username=request_username)
            print("reqeust accepted")
            if not QueryUser and not request.session.get("query_user"):
                
                return JsonResponse({"status" : "failed", "message" :"No user found with the provided username." })
            elif QueryUser or request.session.get("query_user"):
                try:
                    request.session["query_user"] = QueryUser.first().username
                    QueryEmail = QueryUser.first().email
                    request.session["query_email"] = QueryEmail
                
                except:
                    pass
                # Sending the email upon reqeust
                if request.session.get("cooldown", None)is None or  time.CheckCooldown(request.session.get("cooldown")):
                    request.session["cooldown"] = time.SetCooldown()
                    server_otp = modules.GenerateOTP(email=request.session.get("query_email"),request=request.session.get("request","generate_otp"))
                    request.session["otp"] = server_otp
                    returnjson["message"] = f"Email has sent to {MaskEmail(request.session.get("query_email"))}"
                    returnjson["status"] = "ok"
                    request.session["otp"] = server_otp
                    
                
                elif not time.CheckCooldown(request.session.get("cooldown")):
                   
                    returnjson["message"] = "Timer is under cooldown"
                if not request.session.get("query_email"):
                    returnjson["message"] = "No email associated with this account."
                    returnjson["status"] = "failed"
            request.session.set_expiry(30000)

            
            return JsonResponse(returnjson)
        
        # Step 2 : Verify OTP
        elif request_type == "verify_otp":
            request_otp = details_pack.get("otp")
            if  str(request_otp) == str(request.session.get("otp")):
                request.session.pop("otp")
                request.session["setup"] = "otp_done"
                returnjson["message"] = "OTP verified successfully."
                returnjson["status"] = "ok"
                return JsonResponse(returnjson)
            else :
                
                returnjson["message"] = "OTP mismatch!!!"
                returnjson["status"] = "failed"
                return JsonResponse(returnjson)
            
        # Step 3 : Set new password
        elif request_type == "submit_password":
            password_one = details_pack.get("password_one")
            password_two = details_pack.get("password_two")
            if password_one != password_two:
                returnjson["message"] = "Passwords mismatch" 
                returnjson["status"] = "failed"
                return JsonResponse(returnjson)
            elif password_one == password_two:
                print("passwords match")
                if request.session.get("setup") == "otp_done":
                    username = request.session.get("username")
                    user = models.User.objects.filter(username=username).first()
                    if user:
                        user.set_password(password_one)
                        user.save()
                        request.session.pop("setup")
                        request.session.pop("username")
                        returnjson["message"] = "Password reset successful."
                        returnjson["status"] = "ok"
                        print("Password reset successful")
                        print(returnjson)
                        return JsonResponse(returnjson)
                    else:
                        print(request.session.get("username","none"))
                        print("User not found")
                        returnjson["message"] = "User not found."
                        returnjson["status"] = "failed"
                        print(returnjson)
                        return JsonResponse(returnjson)
                

        
    
def AdminLogout(request):
    logout(request)
    return HttpResponse("Logout successful")



def x(request):
    return HttpResponseRedirect(request,"dashboard")