from django.contrib import admin

from .models import Feed

class FeedAdmin(admin.ModelAdmin):
    list_display = ('id','user','status',) 

admin.site.register(Feed,FeedAdmin)