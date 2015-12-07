from core.models import Movie


class MovieListMixin(object):

    def get_context_data(self, **kwargs):
        context = super(MovieListMixin, self).get_context_data(**kwargs)
        context['movie_list'] = get_movie_list()
        return context


def get_movie_list():
    movie_list = Movie.objects.all()
    return movie_list
