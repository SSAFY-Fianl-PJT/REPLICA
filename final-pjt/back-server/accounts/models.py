from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    wishlist = models.ManyToManyField(Movie, related_name="wish_users", blank=True)

    def __str__(self):
        return self.username
