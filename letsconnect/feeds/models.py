from django.db import models

from django.contrib.auth.models import User

class Feed(models.Model):
    status = models.TextField()
    created = models.DateTimeField(auto_now_add=True),
    updated = models.DateTimeField(auto_now_add=True),
    user = models.ForeignKey(User,blank=False,related_name="feeds", on_delete=models.CASCADE)

