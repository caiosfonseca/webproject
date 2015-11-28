from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import *

# Create your views here.

@login_required
def home(request):
    c = RequestContext(request)

    return render_to_response('index.html', c)