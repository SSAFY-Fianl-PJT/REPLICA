from django.db import models
from django.conf import settings


class Genre(models.Model):
    genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    video_path = models.CharField(max_length=200, blank=True, null=True)
    popularity = models.FloatField()
    actors = models.JSONField(null=True)
    director = models.CharField(max_length=100, null=True)
    score_average = models.FloatField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return self.title


