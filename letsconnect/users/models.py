from django.db import models

# Create your models here.
from django.contrib.auth.models import User 


class UserFollow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=False, )
    following = models.ForeignKey(User,on_delete=models.CASCADE, blank=False,related_name='following')
    class Meta:
        unique_together = ('user', 'following',)
    
