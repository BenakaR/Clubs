from django.db import models

class Clubs(models.Model):
    clubId = models.IntegerField(primary_key=True)
    clubName = models.CharField(max_length = 100)
    clubImage = models.CharField(max_length = 100)
    clubDesc = models.CharField(max_length = 100)
    dept = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.clubId)

class UserId(models.Model):
    cid = models.ForeignKey(Clubs,on_delete = models.CASCADE)
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)
    isLeader = models.BooleanField(default = False)
    def __str__(self):
        return str(self.id)

class chats(models.Model):
    cid = models.ForeignKey(Clubs,on_delete = models.CASCADE)
    uid = models.ForeignKey(UserId,on_delete = models.CASCADE)
    txt = models.CharField(max_length = 300)
