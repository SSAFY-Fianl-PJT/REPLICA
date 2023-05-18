from . import views
from django.urls import path


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/reviews/', views.movie_review)
]
