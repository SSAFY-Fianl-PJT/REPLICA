from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, MovieDetailSerializer, MovieReviewSerializer
from .models import Movie
from community.models import Review
from django_filters import rest_framework as filters



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-popularity')[:15]  # 상위 15개의 인기 영화 조회
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_id):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        related_movies = Movie.objects.filter(genres__in=movie.genres.all()).exclude(pk=movie_id).order_by('-popularity')[:5]
        # 비슷한 장르 중 인기도 상위 5개 (현재 영화 제외)
        related_serializer = MovieListSerializer(related_movies, many=True)
        data = serializer.data
        data['related_movies'] = related_serializer.data
        return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_review(request, movie_id):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        reviews = Review.objects.filter(movie_id=movie_id)

        if reviews.exists():
            serializer = MovieReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': '아직 리뷰가 없습니다. 리뷰를 남겨보세요!'})


class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='icontains')
    year = filters.NumberFilter(field_name='release_date', lookup_expr='year')

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'year']


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_search(request):
    movies = Movie.objects.all()
    filter = MovieFilter(request.GET, queryset=movies)
    filtered_movies = filter.qs

    if filtered_movies.exists():
        serializer = MovieListSerializer(filtered_movies, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': '해당 조건을 만족하는 영화가 없습니다.'})