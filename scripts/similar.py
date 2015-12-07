from core.models import Movie


def find_similar(movie):

    similar_list = eval(movie.similars_ids)
    for similar_id in similar_list:
        try:
            similar = Movie.objects.get(tmdb_id=similar_id)
            movie.similars.add(similar)
        except Movie.DoesNotExist:
            pass


def get_similars():
    movies = Movie.objects.all()
    for movie in movies:
        find_similar(movie)


if __name__ == '__main__':
    get_similars()
