from django.shortcuts import render

def ArunTailorsView(request):
    return render(request, "employees/aruntailors.html")

def Home(request):
    return render(request, "aruntailors/aruntailors.html")