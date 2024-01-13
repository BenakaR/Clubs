from django.contrib import admin

# Register your models here.
from .models import UserId,Clubs,chats

admin.site.register(Clubs)
admin.site.register(UserId)
admin.site.register(chats)