from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'



    # movie_id = models.IntegerField(unique=True)
    # title = models.CharField(max_length=100)
    # overview = models.TextField(null=True)
    # poster_path = models.CharField(max_length=200, blank=True, null=True)
    # video_path = models.CharField(max_length=200, blank=True, null=True)
    # popularity = models.FloatField()
    # actors = models.JSONField(null=True)
    # director = models.CharField(max_length=100, null=True)
    # score_average = models.FloatField()
    # release_date = models.DateField()
    # genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


# class ArticleSerializer(serializers.ModelSerializer):
#     comment_set = CommentSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     # username = serializers.CharField(source='user.username', read_only=True)

#     class Meta:
#         model = Article
#         fields = '__all__'
#         # read_only_fields = ('user', )



