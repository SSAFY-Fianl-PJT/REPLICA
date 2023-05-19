from . import views
from django.urls import path

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list), # 메인 영화 조회
    path('<int:movie_id>/', views.movie_detail), # 영화 상세 조회
    path('<int:movie_id>/reviews/', views.movie_review), # 영화별 리뷰 조회
    path('search/', views.movie_search), # 검색
    #http://127.0.0.1:8000/movies/search/?title=앤트맨&year=2018 (검색 예시)
    path('<int:movie_id>/wishlist/', views.movie_wishlist), # 위시리스트 추가
    path('/recommend/<username>/', views.movie_recommendation), # 위시리스트 추가
]
