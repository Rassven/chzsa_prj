from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
# from chzsa_prj.accounts.models import *
from .forms import LoginForm


class LogIn(TemplateView):
    # model = TheUser
    # form_class = LoginForm
    success_url = '/accounts/login'
    template_name = '/accounts/login.html'
