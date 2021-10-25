from django.contrib import admin
from .models import UserFollow

class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('id','user_id',"following_id")

admin.site.register(UserFollow, UserFollowAdmin)
