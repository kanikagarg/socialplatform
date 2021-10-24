# from django.db import models
# from django.db.models import fields
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponseRedirect
from django.views.generic.base import RedirectView
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

class FeedListView(LoginRequiredMixin , ListView):
    model = Feed
    context_object_name = 'feeds'
    template_name = 'feeds/feed_list.html'
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.feeds.all()