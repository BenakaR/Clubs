from django.db import models
from django.contrib.auth.models import User


class Clubs(models.Model):
    clubId = models.IntegerField(primary_key=True)
    clubName = models.CharField(max_length = 100)
    clubImage = models.FileField(upload_to="club/static/assets")
    clubDesc = models.CharField(max_length = 100)
    dept = models.CharField(max_length = 100)
    clubLeader = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.clubId)

class UserId(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    cid = models.ForeignKey(Clubs,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    isLeader = models.BooleanField(default = False)
    def __str__(self):
        return str(self.user.username)

class chats(models.Model):
    cid = models.ForeignKey(Clubs,on_delete = models.CASCADE)
    uid = models.ForeignKey(UserId,on_delete = models.CASCADE)
    txt = models.CharField(max_length = 300)