from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserFollow

class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('id','user_id',"following_id")

admin.site.register(UserFollow, UserFollowAdmin)
