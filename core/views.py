from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import ListView
from django.views.generic import DetailView
from braces.views import LoginRequiredMixin
from .models import *


@login_required
def home(request):
    c = RequestContext(request)
    return render_to_response('core/index.html', c)


class MovieListView(LoginRequiredMixin, ListView):

    model = Movie


class MovieDetailView(LoginRequiredMixin, DetailView):

    model = Movie


class PersonListView(LoginRequiredMixin, ListView):

    model = Person


class PersonDetailView(LoginRequiredMixin, DetailView):

    model = Person
