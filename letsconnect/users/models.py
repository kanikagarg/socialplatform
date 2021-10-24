from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

class UserFollow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=False)
    followers = models.ManyToManyField(User, related_name='follower',blank=True)
    following = models.ManyToManyField(User, related_name='following',blank=True)
    
