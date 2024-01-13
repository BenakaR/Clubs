from django.urls import path
from .views import *


urlpatterns = [
    path('',login_page,name='login_page'),
    path('login/',login,name='login'),
    path('home/',home,name='home'),
    path('event/',event,name='event'),
]
