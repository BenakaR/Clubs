from django.db import models

# Create your models here.
class UserId(models.Model):
    id = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)
    isLeader = models.BooleanField(default = False)
