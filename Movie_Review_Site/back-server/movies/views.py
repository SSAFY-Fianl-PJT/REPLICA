from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieListSerializer, MovieDetailSerializer
from community.serializers import ReviewSerializer
from .models import Movie
from community.models import Review
from community.serializers import ReviewSerializer
from .recommend import features_sim_sorted_ind, find_sim_movies, movies_df
from .tfidf import calculate_tfidf

from django.utils import timezone
from django.views.decorators.cache import cache_page




@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 메인 영화 조회
def movie_list(request):
    if request.method == 'GET':
          # 상위 10개의 인기 영화 조회
        movies = Movie.objects.order_by('-popularity')[:20]
        serializer = MovieListSerializer(movies, many=True)
        user = request.user
        # 찜한 영화 목록
        wishlist_movies = user.wishlist.all()
        wishlist_serializer = MovieDetailSerializer(wishlist_movies, many=True)
        # 개봉 예정 영화 목록
        upcoming_movies = Movie.objects.filter(release_date__gte=timezone.now()).order_by('release_date')[:20]
        upcoming_serializer = MovieListSerializer(upcoming_movies, many=True)

        data = {
            'popular_movies': serializer.data,
            'upcoming_movies': upcoming_serializer.data,
            'wishlist': wishlist_serializer.data
        }
        return Response(data)

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
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        # 리뷰 없는 경우
        else:
            return Response({'message': '아직 리뷰가 없습니다. 리뷰를 남겨보세요!'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 영화 검색
def movie_search(request):
    title = request.GET.get('title', '').strip()
    genre = request.GET.get('genre')
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 영화제목 자동완성
def movie_autocomplete(request):
    word = request.GET.get('word', '').strip()
    results=[]
    
    movies  = Movie.objects.filter(title__icontains = word)
    if movies:
        for movie in movies:
            results.append({
                'word' : movie.title
            })
            
    return JsonResponse({'results': results})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
# 리뷰 좋아요
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user.is_authenticated:
        person = request.user

        if person in movie.like_users.all():
            movie.like_users.remove(person)
            message = '좋아요 취소'
        else:
            movie.like_users.add(person)
            message = '좋아요'
        
        movie.like_users_count = movie.like_users.count()
        serializer = MovieDetailSerializer(movie)

        return Response({'message' : message, 'movie' : serializer.data})


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @cache_page(60 * 30)  # 30분 동안 캐시 유지
# 위시리스트 기반 영화 추천
def movie_recommendation(request, username):

    person = get_object_or_404(get_user_model(), username=username)
    wishlist_movies = person.wishlist.all()

    # 위시리스트 있으면 위시리스트 기반 추천
    if wishlist_movies.exists():
        print('있다')
        wishlist_movie_ids = [movie.movie_id for movie in wishlist_movies]
        print(f'위시리스트 {wishlist_movie_ids}')

        # 위시리스트 기반 추천 계산
        similar_movies = find_sim_movies(movies_df, features_sim_sorted_ind, wishlist_movie_ids, 10)
        print('movies', similar_movies)

        movies = []
        # 추천 영화의 인덱스에서 영화 찾아서 추가
        for movieId in similar_movies:
            movie = get_object_or_404(Movie, movie_id=movieId)
            movies.append(movie)
        # 최대 30개만
        if len(movies) > 30:
            serializer = MovieListSerializer(movies[:30], many=True)
        else:
            serializer = MovieListSerializer(movies, many=True)

        return Response(serializer.data)
    # 없으면 인기도 상위 영화 추천
    else:
        popular_movies = Movie.objects.order_by('-popularity')[:30]
        serializer = MovieListSerializer(popular_movies, many=True)
        
        response_data = {
            'movies': serializer.data
        }
        return Response(response_data)

        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@cache_page(60 * 30)  # 30분 동안 캐시 유지
# 키워드 기반 영화 추천
def tfidf_recommend(request):
    keyword = request.GET.get('keyword')

    if not keyword:
        return Response({'message': '키워드를 입력해주세요.'}, status=400)

    recommendations = calculate_tfidf(keyword)
    recommendations = recommendations[:20]
    movie_ids = [recommendation['fields']['movie_id'] for recommendation in recommendations]
    recommended_movies = Movie.objects.filter(movie_id__in=movie_ids)
    serializer = MovieListSerializer(recommended_movies, many=True)
    return Response(serializer.data)