from django.urls import path
from .views import *


urlpatterns = [
    path('',login_page,name='login_page'),
    path('logout/',logingout,name='logout'),
    path('login/',loging,name='login'),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('event/',event,name='event'),
    path('chat/',chat,name='chat'),
    path('chatinput/',chatInput,name='chatInput'),
    path('createclub/',createClub,name='createClub'),
    path('submitclub/',submitClub,name='submitClub'),
    path('createuser/',createUser,name='createUser'),
    path('register/',register,name='register'),
]
