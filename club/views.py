from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


count=0
errors = ""

def createClub(request):
    return render(request,"form.html")

def submitClub(request):
    global errors
    a = request.POST.get("CID")
    b = request.POST.get("CName")
    cc = request.POST.get("Description")
    d = request.POST.get("Department")
    l = request.POST.get("Uid")
    newClub = Clubs(clubId=a, clubName=b, clubDesc=cc, dept=d, clubImage=request.FILES['logos'],clubLeader = l)
    newClub.save()
    ## return login_page(request,"Club Created Successfully.")
    errors = "Club Created Successfully."
    return HttpResponseRedirect(reverse(login_page))

def createUser(request):
    return render(request,"register.html")

def register(request):
    global errors
    a = request.POST.get("usn")
    b = request.POST.get("name")
    cc = request.POST.get("clubid")
    p = request.POST.get("psw")
    pp = request.POST.get("psw-repeat")
    if p!=pp:
        return HttpResponseRedirect(reverse(register))
    newUser = User.objects.create_user(username=a, password=p)
    newUser.save()
    club = Clubs.objects.get(clubId=cc)
    abc = UserId(user = newUser, name = b, cid=club)
    if a == club.clubLeader :
        abc.isLeader = True
    abc.save()
    ## return login_page(request,"Club Created Successfully.")
    errors = "User Created Successfully."
    return HttpResponseRedirect(reverse(login_page))

def login_page(request):
    global errors
    err = errors
    errors = ""
    return render(request,"login.html",{"error_message":err,"login_count":count})

def logingout(request):
    logout(request)
    return HttpResponseRedirect(reverse(login_page))

def loging(request):
    global errors
    '''try:
        club = int(request.POST.get("club"))
    except:
        ## return login_page(request,"Club ID must be an integer.")    // This will change the url to ../login/. So use below line
        errors = "Club ID must be an integer."
        return HttpResponseRedirect(reverse(login_page))'''
    uid = request.POST.get("uid")
    passw = request.POST.get("psw")

    userr = authenticate(request, username = uid, password = passw)
    if userr is not None:
        login(request,userr)
        return HttpResponseRedirect(reverse(home))
    else:
        errors = "Wrong Credentials"
        return HttpResponseRedirect(reverse(login_page))


@login_required(login_url='login_page')
def home(request):
    img = UserId.objects.get(user=request.user).cid.clubImage
    file = img.name[len("club/static/") : ]
    context = { 'username':request.user.username,
               'clubId':UserId.objects.get(user=request.user).cid.clubId,
               'logo':file
                 }
    return render(request,"home.html",context)

@login_required(login_url='login_page')
def about(request):
    context = { 'username':request.user.username,
               'clubId':UserId.objects.get(user=request.user).cid.clubId
                 }
    return render(request,"about.html",context)

@login_required(login_url='login_page')
def event(request):
    context = { 'username':request.user.username,
               'clubId':UserId.objects.get(user=request.user).cid.clubId
                 }
    return render(request,"event.html",context)

@login_required(login_url='login_page')
def chat(request):
    chatss = chats.objects.all
    context = {'username':request.user.username,
               'clubId':UserId.objects.get(user=request.user).cid.clubId,
               'chatss':chatss
                 }
    return render(request,"chat.html",context)

@login_required(login_url='login_page')
def chatInput(request):
    texts = request.POST.get("inputs")
    if texts==None or texts=="":
        return chat(request)
    c = chats()
    c.cid=Clubs.objects.get(clubId=UserId.objects.get(user=request.user).cid.clubId)
    c.uid=UserId.objects.get(user=request.user)
    c.txt = texts
    c.save()
    return HttpResponseRedirect(reverse(chat))


