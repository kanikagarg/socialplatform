from django.urls import path
from feeds import views

urlpatterns = [
    path('',views.FeedListView.as_view(), name="feed.list"),
    path('new/',views.FeedsCreateView.as_view(), name="feed.create"),
]