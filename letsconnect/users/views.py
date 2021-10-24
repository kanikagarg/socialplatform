# from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.views import LoginView, LogoutView
# from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    template_name = "user/register.html"
    form_class = UserCreationForm
    success_url="/feeds"
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            redirect("/feeds")
        return super().get(self, request, *args, **kwargs)

class LoginUserView(LoginView):
    model = User
    template_name = "user/login.html"

class LogoutUserView(LogoutView):
    model = User
    template_name = "user/logout.html"

class UserListView(LoginRequiredMixin , ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user/list.html'
    login_url = "/login"

    def get_queryset(self):
        id = self.request.user.id
        print(id)
        users = User.objects.exclude(pk=id)
        return users