from django.http.response import Http404, HttpResponseRedirect
# from django.views.generic.base import RedirectView
# from django.shortcuts import render

from .models import Feed
from django.views.generic import ListView, DetailView,CreateView
from .forms import FeedForm
from django.contrib.auth.mixins import LoginRequiredMixin

class FeedsCreateView(LoginRequiredMixin , CreateView):
    model=Feed
    success_url = "/feeds"
    form_class = FeedForm
    login_url = "/login"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        success_url = self.get_success_url()
        print(success_url)
        return HttpResponseRedirect(self.get_success_url())

from users.models import UserFollow
class FeedListView(LoginRequiredMixin , ListView):
    model = Feed
    context_object_name = 'feeds'
    template_name = 'feeds/feed_list.html'
    login_url = "/login"
    def get_queryset(self):
        logged_user_id = self.request.user.id
        following_id =[]
        for mapping in UserFollow.objects.filter(user_id=logged_user_id):
            following_id.append(mapping.following.id)
        feeds = Feed.objects.filter(user_id__in=following_id).order_by('?')
        return feeds
        # return self.request.user.feeds.all()