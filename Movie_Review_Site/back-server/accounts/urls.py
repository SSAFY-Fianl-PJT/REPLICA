from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'), # 프로필
    path('<username>/follow/', views.follow, name='follow'), # 유저 팔로우
    path('my_wishlist/<username>/', views.wishlist, name='wishlist'), # 위시리스트
]
