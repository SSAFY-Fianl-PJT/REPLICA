from rest_framework import serializers
from .models import Movie, Genre
from community.models import Review

# 장르
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

# 영화 목록
class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

# 영화 상세
class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

# 영화별 리뷰
class MovieReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
