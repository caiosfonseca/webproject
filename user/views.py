from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from user.mixins import SuccessMixin
from user.forms import RegisterForm


class RegisterView(SuccessMixin, CreateView):

    model = User
    form_class = RegisterForm
    success_message = 'User created with success!'
    success_url = reverse_lazy('auth:login')


register = RegisterView.as_view()
