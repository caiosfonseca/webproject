from django.db import models
from django.contrib.auth.models import User
from core.enum import PERSON_JOB
from core.enum import VOTE_STATUS


class Movie(models.Model):

    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    popularity = models.DecimalField(max_digits=4, decimal_places=2)
    poster_path = models.URLField()
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=4, decimal_places=2)

    genres = models.ManyToManyField('Genre')

    directors = models.ManyToManyField('Person', related_name='directors',
                                       null=True, blank=True)
    producers = models.ManyToManyField('Person', related_name='producerts',
                                       null=True, blank=True)
    casting = models.ManyToManyField('Person', related_name='casting',
                                       null=True, blank=True)

    similars = models.ManyToManyField('Movie', null=True, blank=True)



class Person(models.Model):

    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    job = models.IntegerField(choices=PERSON_JOB)
    nickname = models.CharField(max_length=255)
    biography = models.TextField(null=True, blank=True)
    birthday = models.DateField()
    deathday = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255)
    popularity = models.DecimalField(max_digits=4, decimal_places=2)
    profile_path = models.URLField()


class Genre(models.Model):

    name = models.CharField(max_length=255)
    genre_id = models.IntegerField()


class Vote(models.Model):

    user = models.ForeignKey(User)
    movies = models.ForeignKey('Movie')
    status = models.IntegerField(choices=VOTE_STATUS)
