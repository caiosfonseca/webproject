from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from braces.views import LoginRequiredMixin
from core.models import Movie, Person
from core.mixins import MovieListMixin, get_movie_list, register_vote
from core.mixins import PeopleListMixin, get_people_list
from core.mixins import GetVoteMixin


class HomeView(LoginRequiredMixin, MovieListMixin, TemplateView):

    template_name = 'core/index.html'


class MovieListView(LoginRequiredMixin, MovieListMixin, ListView):

    model = Movie


class MovieDetailView(LoginRequiredMixin, MovieListMixin, GetVoteMixin, DetailView):

    model = Movie


class PersonListView(LoginRequiredMixin, PeopleListMixin, ListView):

    model = Person


class PersonDetailView(LoginRequiredMixin, PeopleListMixin, DetailView):

    model = Person


class MovieSearchView(LoginRequiredMixin, View):

    template_name = 'core/movie_list.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        try:
            movie = Movie.objects.get(title=query)
            redirect_url = reverse_lazy('core:movie_detail', args=[movie.pk])
            return HttpResponseRedirect(redirect_url)
        except Movie.DoesNotExist:
            movies = Movie.objects.filter(title__icontains=query)
            context = {'object_list': movies, 'movie_list': get_movie_list()}
            return render(request, self.template_name, context)

class PersonSearchView(LoginRequiredMixin, View):

    template_name = 'core/people_list.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        try:
            person = Person.objects.get(name=query)
            redirect_url = reverse_lazy('core:person_detail', args=[person.pk])
            return HttpResponseRedirect(redirect_url)
        except Person.DoesNotExist:
            peoples = Person.objects.filter(name__icontains=query)
            context = {'object_list': peoples, 'people_list': get_people_list()}
            return render(request, self.template_name, context)


class VoteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        movie = Movie.objects.get(pk=kwargs['pk'])
        status = kwargs['status']
        user = self.request.user
        register_vote(user, movie, status)
        redirect_url = reverse_lazy('core:movie_detail', args=[movie.id])
        return HttpResponseRedirect(redirect_url)
