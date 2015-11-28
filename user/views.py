from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.base import RedirectView

from braces.views import LoginRequiredMixin

from user.mixins import SuccessMixin
from user.forms import LoginForm
from user.forms import RegisterForm
from user.forms import ChangePasswordForm
from user.forms import RememberPasswordForm


class LoginView(login):

    template_name = 'user/login.html'
    authentication_form = LoginForm


class RegisterView(SuccessMixin, CreateView):

    model = User
    form_class = RegisterForm
    success_message = 'User created with success!'
    success_url = reverse_lazy('auth:login')


class ChangePasswordView(LoginRequiredMixin, SuccessMixin, FormView):

    form_class = ChangePasswordForm
    success_message = 'Password modified with success!'
    success_url = reverse_lazy('core:home')


class RememberPasswordView(SuccessMixin, FormView):

    form_class = RememberPasswordForm
    success_message = 'New password sent to your email address!'
    success_url = reverse_lazy('auth:login')


class LogoutView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_success_url(self):
        logout(self.request)
        return reverse_lazy('auth:login')


login = LoginView.as_view()
logout_view = LogoutView.as_view()
register = RegisterView.as_view()
change_password = ChangePasswordView.as_view()
remember_password = RememberPasswordView.as_view()
