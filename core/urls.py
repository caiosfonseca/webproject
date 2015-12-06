from django.conf.urls import url

from .views import HomeView
from .views import VoteView
from .views import MovieListView
from .views import MovieDetailView
from .views import MovieSearchView
from .views import PersonListView
from .views import PersonDetailView
from .views import PersonSearchView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^movies/$', MovieListView.as_view(), name='movies_list'),
    url(r'^movie/(?P<pk>[\d]+)/$', MovieDetailView.as_view(),
        name='movie_detail'),
    url(r'^movies_search/$', MovieSearchView.as_view(),
        name='movies_search'),
    url(r'^people/$', PersonListView.as_view(), name='people_list'),
    url(r'^person/(?P<pk>[\d]+)/$', PersonDetailView.as_view(),
        name='person_detail'),
    url(r'^people_search/$', PersonSearchView.as_view(),
        name='people_search'),
    url(r'^vote/(?P<pk>[\d]+)/(?P<status>[\w]+)/$', VoteView.as_view(),
        name='vote')
]
