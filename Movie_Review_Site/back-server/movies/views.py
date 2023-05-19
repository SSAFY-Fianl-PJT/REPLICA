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
# from django_filters import rest_framework as filters
from django.utils import timezone
from django.db.models import Q


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
# 메인 영화 조회
def movie_list(request):
    if request.method == 'GET':
          # 상위 10개의 인기 영화 조회
        movies = Movie.objects.order_by('-popularity')[:10]
        serializer = MovieListSerializer(movies, many=True)
        user = request.user
        # 찜한 영화 목록
        wishlist_movies = user.wishlist.all()
        wishlist_serializer = MovieDetailSerializer(wishlist_movies, many=True)
        # 개봉 예정 영화 목록
        upcoming_movies = Movie.objects.filter(release_date__gte=timezone.now()).order_by('release_date')[:10]
        upcoming_serializer = MovieListSerializer(upcoming_movies, many=True)

        data = {
            'popular_movies': serializer.data,
            'upcoming_movies': upcoming_serializer.data,
            'wishlist': wishlist_serializer.data
        }
        return Response(data)

    elif request.method == 'POST':
        serializer = MovieDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 영화 상세 조회
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        # 비슷한 장르 중 인기도 상위 5개 (현재 영화 제외)
        related_movies = Movie.objects.filter(genres__in=movie.genres.all()).exclude(pk=movie_id).order_by('-popularity')[:5]
        related_serializer = MovieListSerializer(related_movies, many=True)
        data = serializer.data
        # 연관 영화 함께 반환
        data['related_movies'] = related_serializer.data
        return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 영화별 리뷰 조회
def movie_review(request, movie_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie_id=movie_id)

        if reviews.exists():
            serializer = MovieReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        # 리뷰 없는 경우
        else:
            return Response({'message': '아직 리뷰가 없습니다. 리뷰를 남겨보세요!'})


# # 검색 조건
# class MovieFilter(filters.FilterSet):
#     title = filters.CharFilter(lookup_expr='icontains')
#     genres = filters.CharFilter(field_name='genres__name', lookup_expr='icontains')
#     year = filters.NumberFilter(field_name='release_date', lookup_expr='year')

#     class Meta:
#         model = Movie
#         fields = ['title', 'genres', 'year']


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 영화 검색
def movie_search(request):
    title = request.GET.get('title')
    genre = request.GET.get('genre', '')
    year = request.GET.get('year')

    movies = Movie.objects.all()

    if title:
        movies = movies.filter(title__icontains=title)

    if genre:
        movies = movies.filter(genres__genre_name__icontains=genre)

    if year:
        movies = movies.filter(release_date__year=year)

    if movies.exists():
        movies = movies[:50]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': '해당 조건을 만족하는 영화가 없습니다.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
# 위시 리스트 추가/제거
def movie_wishlist(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)

    # 현재 찜해놓은 경우 제거
    if movie in request.user.wishlist.all():
        request.user.wishlist.remove(movie)
        message = f'{movie.title}을(를) 찜 목록에서 제거했습니다.'
    # 현재 찜 해놓지 않은 경우에는 추가
    else:
        request.user.wishlist.add(movie)
        message = f'{movie.title}을(를) 찜 목록에 추가했습니다.'

    serializer = MovieDetailSerializer(movie)
    response_data = {
        'message': message,
        'profile': serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)