import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
from .models import Movie
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# with open('Movie_Review_Site/back-server/movies/fixtures/movie_data.json', encoding='utf-8') as file:
#     data = json.load(file)


# movies = data  # JSON 데이터에서 영화 리스트 추출
# movie_data = []

# csv 생성
# for movie in movies:
#     movie_id = movie['pk']
#     title = movie['fields']['title']
#     release_date = movie['fields']['release_date']
#     popularity = movie['fields']['popularity']
#     score_average = movie['fields']['score_average']
#     overview = movie['fields']['overview']
#     poster_path = movie['fields']['poster_path']
#     genres = ', '.join(str(genre) for genre in movie['fields']['genres'])
#     director = movie['fields']['director']
#     actors = ', '.join(actor for actor in movie['fields']['actors'])
    
#     movie_data.append([movie_id, title, release_date, popularity, score_average, overview, poster_path, genres, director, actors])

# columns = ['movie_id', 'title', 'release_date', 'popularity', 'score_average', 'overview', 'poster_path', 'genres', 'director', 'actors']
# df = pd.DataFrame(movie_data, columns=columns)
# df.to_csv('movies.csv',encoding='utf-8', index=False)

movies=pd.read_csv("C:/SSAFY/1학기 최종/Movie_Review_Site/back-server/movies/movies.csv")
# print(movies.shape) # (4992, 10)
# movies.head(1)

# 주요 칼럼 추출
movies_df=movies[['movie_id', 'title', 'genres', 'release_date', 'score_average', 'popularity', 'actors', 'director']]
movies_df.head(8)
# movies_df[['actors']][:1]

# genre, actors, director, title기반으로 코사인 유사도 계산
movies_df['features'] = movies_df['genres'] + ' ' + movies_df['actors'] + ' ' + movies_df['title'] +  ' ' + movies_df['director']
movies_df['features'] = movies_df['features'].fillna('')  # NaN 값을 빈 문자열로 대체
count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))
features_mat = count_vect.fit_transform(movies_df['features'])
print(features_mat.shape)

# 피처 백터화한 행렬로 계산
features_sim = cosine_similarity(features_mat, features_mat)
print(features_sim.shape)
print(features_sim[:1])

# 유사도 높은 순 정렬
features_sim_sorted_ind = features_sim.argsort()[:, ::-1]
print(features_sim_sorted_ind[:1])

# def find_sim_movie(df, sorted_ind, title_names, top_n=10):
def find_sim_movie(movie_id, sorted_ind, top_n=10):
    # movie_id에 해당하는 인덱스 추출
    movie_index = movies_df[movies_df['movie_id'] == movie_id].index.values
    # top_n의 2배에 해당하는 장르 유사성이 높은 인덱스 추출
    similar_indexes = sorted_ind[movie_index, :(top_n*2)]
    # reshape(-1) 1차원 배열로 변환
    similar_indexes = similar_indexes.reshape(-1)
    # 기준 영화 인덱스는 제외
    similar_indexes = similar_indexes[similar_indexes != movie_index]

    similar_movies = Movie.objects.filter(movie_id__in=movies_df.iloc[similar_indexes]['movie_id'])

    return similar_movies
    # similar_movies = pd.DataFrame()
    
    # for title_name in title_names:
    #     movie = df[df['title'] == title_name]
    #     movie_index = movie.index.values
    #     # top_n의 2배에 해당하는 장르 유사성이 높은 인덱스 추출
    #     similar_indexes = sorted_ind[movie_index, :(top_n*2)]
    #     # reshape(-1) 1차열 배열 반환
    #     similar_indexes = similar_indexes.reshape(-1)
    #     # 기준 영화 인덱스는 제외
    #     similar_indexes = similar_indexes[similar_indexes != movie_index]

    #     similar_movies = pd.concat([similar_movies, df.iloc[similar_indexes]])

    # # 코사인 유사도 점수가 높은 순으로 정렬
    # similar_movies = similar_movies.drop_duplicates()  # 중복 영화 제거
    # similar_movies = similar_movies.sort_values('features_sim', ascending=False)[:top_n]
    
    # return similar_movies

# movies_df['features_sim'] = np.nan  # features_sim 열 초기화
# similar_movies = find_sim_movie(movies_df, features_sim_sorted_ind, user_wishlist, 10)
# similar_movies[['title', 'release_date', 'score_average', 'features_sim']]


