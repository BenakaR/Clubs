from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

username = 0
clubNo = 0

def login_page(request):
    return render(request,"login.html")

def login(request):
    club = int(request.POST.get("club"))
    names = request.POST.get("uname")
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
        if user.password == passw and user.cid.clubId == club :
            global username,clubNo
            username=user.id
            clubNo = club
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
    if username=='' or clubNo == 0:
        return render(request,"login.html")
    return render(request,"home.html",{'username':username,'clubId':clubNo})

def about(request):
    if username=='' or clubNo == 0:
        return render(request,"login.html")
    return render(request,"about.html",{'username':username,'clubId':clubNo})

def event(request):
    if username=='' or clubNo == 0:
        return render(request,"login.html")
    return render(request,"event.html",{'username':username,'clubId':clubNo})

def chat(request):
    chatss = chats.objects.all
    if username=='' or clubNo == 0:
        return render(request,"login.html")
    return render(request,"chat.html",{'username':username,'clubId':clubNo,'chatss':chatss})

def chatInput(request):
    texts = request.POST.get("inputs")
    c = chats()
    c.cid=Clubs.objects.get(clubId=clubNo)
    c.uid=UserId.objects.get(id=username)
    c.txt = texts
    c.save()
    chatss = chats.objects.all
    if username=='' or clubNo == 0:
        return render(request,"login.html")
    return render(request,"chat.html",{'username':username,'clubId':clubNo,'chatss':chatss})

def createClub(request):
    return render(request,"form.html")

def submitClub(request):
    a = request.POST.get("CID")
    b = request.POST.get("CName")
    cc = request.POST.get("Description")
    d = request.POST.get("Department")
    newClub = Clubs(clubId=a, clubName=b,dept = d)
    newClub.save()
    return render(request,"login.html",{'error_message':"Club created"})
