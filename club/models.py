from django.db import models

# Create your models here.
class UserId(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length = 100,primary_key = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)
    isLeader = models.BooleanField(default = False)
