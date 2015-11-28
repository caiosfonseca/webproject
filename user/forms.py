from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
