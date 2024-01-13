from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

username = ''
# Create your views here.
def login_page(request):
    return render(request,"login.html")

def login(request):
    names = request.POST.get("uname")
    print(names)
    passw = request.POST.get("psw")
    try:
        user = UserId.objects.get(name=names)
    except :
        return render(
            request,
            "login.html",
            {
                "error_message": "Username not found.",
            },
        )
    else:
        if user.password == passw:
            global username
            username=names
            return render(request,"home.html",{'username':username})
        else:
            return render(
                request,
                "login.html",
                {
                    "error_message": "Wrong Password.",
            },
            )
        
def home(request):
    if username=='':
        return render(request,"login.html")
    return render(request,"home.html",{'username':username})

def event(request):
    if username=='':
        return render(request,"login.html")
    return render(request,"event.html",{'username':username})