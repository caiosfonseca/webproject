from collections import Counter, OrderedDict
from core.models import *


def recommendations_by_user(user):

    votes = Vote.objects.filter(status='like', user=user).order_by('-date')
    movies_ids = votes.values_list('movie', flat=True)[:5]

    movies = Movie.objects.filter(id__in=movies_ids)
    people = get_people_from_movies(movies)
    genres = get_genres_from_movies(movies)

    recommendations = []
    recommendations.append(recommendations_most_popular())
    recommendations.append(recommendations_top_rated())
    for movie in movies:
        recommendations.append(recommendations_by_movie(movie))
    for person in people:
        recommendations.append(recommendations_by_person(person))
    for genre in genres:
        recommendations.append(recommendations_by_genre(genre))

    return recommendations


def recommendations_most_popular():

    name = 'Most popular movies'
    movies = Movie.objects.all().order_by('-popularity')[:30]
    return {'name': name, 'movies': movies}


def recommendations_top_rated():

    name = 'Top rated movies'
    movies = Movie.objects.filter(
        vote_count__gte=1000
    ).order_by('-vote_average')[:30]
    return {'name': name, 'movies': movies}


def recommendations_by_movie(movie):

    name = 'Because you liked {0}'.format(movie.title)
    movies = movie.similars.all().order_by('popularity')
    return {'name': name, 'movies': movies}


def recommendations_by_person(person):

    name = 'Top movies with {0}'.format(person.name)
    movies = []
    movies += Movie.objects.filter(casting__in=[person])
    movies += Movie.objects.filter(directors__in=[person])
    movies += Movie.objects.filter(producers__in=[person])
    movies = sorted(set(movies), key=lambda x: x.popularity, reverse=True)
    return {'name': name, 'movies': movies}


def recommendations_by_genre(genre):

    name = 'Most popular {0} movies'.format(genre.name)
    movies = Movie.objects.filter(
        genres__in=[genre]
    ).order_by('-popularity')[:30]
    return {'name': name, 'movies': movies}


def get_people_from_movies(movies):
    """Returns the five most popular people among the movies"""
    people_ids = []
    for movie in movies:
        people_ids += movie.casting.all().values_list('id', flat=True)
        people_ids += movie.directors.all().values_list('id', flat=True)
        people_ids += movie.producers.all().values_list('id', flat=True)
    people = Person.objects.filter(
        id__in=people_ids
    ).order_by('-popularity')[:5]
    return people


def get_genres_from_movies(movies):
    """Returns the three most liked genres among the movies"""

    genres_ids = []
    for movie in movies:
        genres_ids += movie.genres.all().values_list('id', flat=True)
    counter = Counter(genres_ids).most_common()
    most_frequent = [pk for (pk, count) in counter][:5]
    genres = Genre.objects.filter(id__in=most_frequent).order_by('name')
    return genres
