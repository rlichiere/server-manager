from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput


class FrontAuthForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput())
