import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')

from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

with open('Movie_Review_Site/back-server/movies/fixtures/movie_data.json', encoding='utf-8') as file:
    data = json.load(file)


movies = data  # JSON 데이터에서 영화 리스트 추출
movie_data = []

for movie in movies:
    movie_id = movie['pk']
    title = movie['fields']['title']
    release_date = movie['fields']['release_date']
    popularity = movie['fields']['popularity']
    score_average = movie['fields']['score_average']
    overview = movie['fields']['overview']
    poster_path = movie['fields']['poster_path']
    genres = ', '.join(str(genre) for genre in movie['fields']['genres'])
    director = movie['fields']['director']
    actors = ', '.join(actor for actor in movie['fields']['actors'])
    
    movie_data.append([movie_id, title, release_date, popularity, score_average, overview, poster_path, genres, director, actors])

columns = ['movie_id', 'title', 'release_date', 'popularity', 'score_average', 'overview', 'poster_path', 'genres', 'director', 'actors']
df = pd.DataFrame(movie_data, columns=columns)
df.to_csv('movies.csv', index=False)
