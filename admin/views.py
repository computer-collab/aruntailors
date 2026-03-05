from django.shortcuts import render
from django.http import request,JsonResponse
import json

def AdminLogin(request):
    if request.method == "GET":
        return render(request,"admin/admin_login.html")
    
    elif request.method == "POST":
        login_pack = json.loads(request.body)
        return JsonResponse(""" {
                            "message" : "Json recieved"}  """)
        