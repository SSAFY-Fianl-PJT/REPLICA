from . import views
from django.urls import path


app_name = 'community'
urlpatterns = [
    path('', views.review_list, name='list'), # 리뷰 목록
    path('<int:review_id>/', views.review_detail, name='detail'), # 리뷰 상세
    path('<int:review_id>/like/', views.review_like, name='like'), # 리뷰 좋아요
    path('<int:review_id>/comments/', views.comments, name='comments'), # 리뷰별 댓글
    path('<int:review_id>/comments/<int:comment_id>/', views.comment_update, name='comment_update'), # 댓글 수정
]
