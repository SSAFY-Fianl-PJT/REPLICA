from movies import views
from django.urls import path


app_name = 'movies'
urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_id>/', views.movie_detail),
]
