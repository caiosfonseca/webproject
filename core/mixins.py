from core.models import Movie
from core.models import Vote
from core.models import Person


class MovieListMixin(object):

    def get_context_data(self, **kwargs):
        context = super(MovieListMixin, self).get_context_data(**kwargs)
        context['movie_list'] = get_movie_list()
        return context


def get_movie_list():
    movie_list = Movie.objects.all()
    return movie_list


def register_vote(user, movie, status):

    try:
        vote = Vote.objects.get(movie=movie, user=user)
        vote.status = status
        vote.save()
    except Vote.DoesNotExist:
        Vote.objects.create(movie=movie, user=user, status=status)


class GetVoteMixin(object):

    def get_context_data(self, **kwargs):
        context = super(GetVoteMixin, self).get_context_data(**kwargs)
        try:
            movie = context['movie']
            user = self.request.user
            vote = Vote.objects.get(movie=movie, user=user)
        except:
            vote = None
        context['vote'] = vote
        return context

class PeopleListMixin(object):

    def get_context_data(self, **kwargs):
        context = super(PeopleListMixin, self).get_context_data(**kwargs)
        context['people_list'] = get_people_list()
        return context


def get_people_list():
    people_list = Person.objects.all()
    return people_list
