from django.urls import path
from .views import *


urlpatterns = [
    path('',login_page,name='login_page'),
    path('login/',login,name='login'),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('event/',event,name='event'),
    path('chat/',chat,name='chat'),
    path('chat/',chatInput,name='chatInput'),
    path('createclub/',createClub,name='createClub'),
    path('submitclub/',submitClub,name='submitClub'),
]
