# from django import forms
from django.contrib.auth.forms import AuthenticationForm   # UserCreationForm, BaseUserCreationForm
# from ..accounts.models import OrganizationGroup, TheOrganization
# from allauth.account.forms import SignupForm


class LoginForm(AuthenticationForm):
    fields = ('__all__', )
