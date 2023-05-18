from . import views
from django.urls import path


app_name = 'community'
urlpatterns = [
    path('', views.review_list, name='list'),
    path('<int:review_id>/', views.review_detail, name='detail'),
    path('<int:review_id>/comments/', views.comments, name='comments'),
    path('<int:review_id>/comments/<int:comment_id>', views.comment_update, name='comment_update'),
]
