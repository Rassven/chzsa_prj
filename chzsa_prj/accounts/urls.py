from django.urls import path
from .views import LogIn, LogOut, TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('signup/', SignUp.as_view(), name='signup'),
    # path('login/', LogIn.as_view(), name='login'),
    # path('/logout', LogOut.as_view(), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
