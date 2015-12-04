from django.conf.urls import url

from .views import home
from .views import MovieListView
from .views import MovieDetailView
from .views import PersonListView
from .views import PersonDetailView

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^movies/$', MovieListView.as_view(), name='movies_list'),
    url(r'^movie/(?P<pk>[\d]+)/$', MovieDetailView.as_view(),
        name='movie_detail'),
    url(r'^people/$', PersonListView.as_view(), name='people_list'),
    url(r'^person/(?P<pk>[\d]+)/$', PersonDetailView.as_view(),
        name='person_detail'),
]
