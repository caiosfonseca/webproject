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
                                       blank=True)
    producers = models.ManyToManyField('Person', related_name='producerts',
                                       blank=True)
    casting = models.ManyToManyField('Person', related_name='casting',
                                     blank=True)

    similars = models.ManyToManyField('Movie', blank=True)
    similars_ids = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Person(models.Model):

    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    deathday = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, null=True, blank=True)
    popularity = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    profile_path = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):

    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vote(models.Model):

    user = models.ForeignKey(User)
    movies = models.ForeignKey('Movie')
    status = models.IntegerField(choices=VOTE_STATUS)
