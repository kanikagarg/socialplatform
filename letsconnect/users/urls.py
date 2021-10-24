from users import views
from django.urls import path
urlpatterns =[
    path('login/',  views.LoginUserView.as_view(), name="login" ),
    path('logout/', views.LogoutUserView.as_view(), name="logout" ),
    path('signup/', views.RegisterView.as_view(), name="register" ),
    path('list/', views.UserListView.as_view(), name="list"),
    path('',  views.LoginUserView.as_view()),
]
