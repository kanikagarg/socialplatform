from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import UserFollow


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
    def form_valid(self, form):
        return redirect(self.get_success_url())

class LogoutUserView(LogoutView):
    model = User
    template_name = "user/logout.html"

class UserListView(LoginRequiredMixin , ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user/list.html'
    login_url = "/login"

    def get_queryset(self):
        filter_on = self.request.session.get("fuser")
        filtereduser = User.objects.filter(username__icontains=filter_on)
        return filtereduser


@login_required(login_url='/login')
def search(request):
        if request.method == 'POST':
            for key,val in request.POST.items():
                if key=="searchuser":
                    user=val            
                    # sets serched user keyword in session
                    request.session['fuser']=user
                    request.session.modified=True
                    # print(request.session.get('fuser',"USERSESSIONIDFI"))
            obj = {
                "users": User.objects.filter(username__contains=user)
            }
            return redirect('/list/')
        else:
            filtereduser = request.session.get("fuser")
            obj = {
                "users":User.objects.filter(username__icontains=filtereduser)
            }
            return render("request",'user/search.html', obj)


# function to follow a user
@login_required(login_url='/login')
def followUser(request, uid):
    try:
        follower_following_mapping = UserFollow.objects.create(user_id=request.user.id, 
        following=User.objects.get(pk=uid))
        follower_following_mapping.save()
        return render(request,"user/followed.html",{"msg":"User followed successfully!"})
    except Exception as e:
        print(e)
        return render(request,"user/followed.html",{"msg":"Something went wrong!!!"})



# function to check if the user is already followed or not
# TO DO - implement with ajax
@login_required(login_url='/login')
def checkUserFollowedStatus(request, uid):
    try:
        current_user = request.user.id
        follower_following_mapping = UserFollow.objects.get(user_id=current_user, 
        following=User.objects.get(pk=uid))
        
        if follower_following_mapping:
            return True
        else:
            return False
    except Exception as e:
        print(e, "err when following {} by user {}".format(uid,current_user))
        return False

    