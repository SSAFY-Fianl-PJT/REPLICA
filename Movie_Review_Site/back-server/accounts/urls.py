from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user-info/', views.get_user_info, name='user-info'), # 유저 정보
    path('profile/<username>/', views.profile, name='profile'), # 프로필
    path('<username>/follow/', views.follow, name='follow'), # 유저 팔로우
    path('my_wishlist/<username>/', views.user_wishlist, name='wishlist'), # 위시리스트
    path('user-delete/<int:user_id>/', views.user_delete, name='user-delete'), # 유저삭제
]
