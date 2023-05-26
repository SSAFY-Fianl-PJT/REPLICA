import requests
import json

TMDB_API_KEY = '3fe19e4ee741c6f09c43b338efe4ec41'
def get_movie_datas():
    total_data = []

    # 1페이지부터 250페이지까지 (페이지당 20개, 총 5,000개)
    for i in range(1, 251):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'score_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'director': '',
                    'actors':[],
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }
                total_data.append(data)
        if i % 10 == 0:
            print(movie['title'])
        
        # 감독/배우 정보가 있는 경우, 추가로 받아온다.
    for data in total_data:
        movie_id = data['fields']['movie_id']
        
        credit_request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
        credit_info = requests.get(credit_request_url).json()

        # 배우는 최대 5명까지만 저장한다.
        for cast in credit_info['cast'][:5]:
            data['fields']['actors'].append(cast['name'])
        
        if credit_info['crew']:
            data['fields']['director'] = credit_info['crew'][0]['name']
            print(credit_info['crew'][0]['name'])

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

# get_movie_datas()
