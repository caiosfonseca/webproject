from django.db import models
from django.contrib.auth.models import User


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

    class Meta:
        ordering = ['-popularity', '-vote_average']


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

    class Meta:
        ordering = ["-popularity", 'name']


class Genre(models.Model):

    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Vote(models.Model):

    VOTE_STATUS = (
        ('dislike', 'Dislike'),
        ('like', 'Like')
    )

    user = models.ForeignKey(User)
    movie = models.ForeignKey('Movie')
    status = models.CharField(max_length=7, choices=VOTE_STATUS)
    date = models.DateTimeField(auto_now_add=True)
