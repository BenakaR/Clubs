from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

username = 0
clubNo = 0

def login_page(request,errors=None):
    return render(request,"login.html",{"error_message":errors})

def login(request):
    try:
        club = int(request.POST.get("club"))
    except:
        return login_page(request,"Club ID must be an integer.")
    id = request.POST.get("uid")
    passw = request.POST.get("psw")
    try:
        user = UserId.objects.get(id=id)
    except :
        return login_page(request,"User ID not found")
    else:
        if user.password == passw and user.cid.clubId == club :
            global username,clubNo
            username=user.id
            clubNo = club
            return home(request)
        else:
            if user.cid.clubId != club:
                return login_page(request,"Wrong Club ID.")
            else:
                return login_page(request,"Wrong Password.")
        
def home(request):
    if username=='' or clubNo == 0:
        return render(request,"login.html")
    img = Clubs.objects.get(clubId = clubNo).clubImage
    file = img.name[len("club/static/") : ]
    return render(request,"home.html",{'username':username,'clubId':clubNo,'logo':file})

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
    if texts==None or texts=="":
        return chat(request)
    c = chats()
    c.cid=Clubs.objects.get(clubId=clubNo)
    c.uid=UserId.objects.get(id=username)
    c.txt = texts
    c.save()
    return chat(request)

def createClub(request):
    return render(request,"form.html")

def submitClub(request):
    a = request.POST.get("CID")
    b = request.POST.get("CName")
    cc = request.POST.get("Description")
    d = request.POST.get("Department")
    newClub = Clubs(clubId=a, clubName=b, clubDesc=cc, dept=d, clubImage=request.FILES['logos'])
    newClub.save()
    return login_page(request,"Club Created Successfully.")
