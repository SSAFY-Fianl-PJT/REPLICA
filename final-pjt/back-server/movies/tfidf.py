import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from functools import lru_cache
import os
from functools import lru_cache
dir_path = os.path.dirname(os.path.abspath(__file__))

# 영화 데이터 파일 경로
movie_data_file = os.path.join(dir_path, "fixtures/movie_data.json")

@lru_cache(maxsize=128)  # 모든 호출 결과를 캐시에 저장
def calculate_tfidf(keyword):
    # JSON 파일 불러오기
    with open(movie_data_file, "r", encoding='utf-8') as json_file:
        movie_data = json.load(json_file)

    # 추천 영화 목록 생성
    recommendations = []

    # TF-IDF 벡터화
    corpus = [movie['fields']['overview'] for movie in movie_data]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # 입력값에 대한 TF-IDF 벡터 계산
    input_tfidf = vectorizer.transform([keyword])
    print('입력', input_tfidf)

    # 코사인 유사도 계산
    similarity_scores = cosine_similarity(input_tfidf, tfidf_matrix)
    print('유사도', similarity_scores)

    # 유사도가 높은 순으로 추천 영화 선정
    similar_indices = [i for i in similarity_scores.argsort().flatten()[::-1] if similarity_scores[0, i] > 0]
    print('tfidi', similar_indices)
    for idx in similar_indices:
        recommendations.append(movie_data[idx])
    # print(recommendations[:20])

    cache_info = calculate_tfidf.cache_info()
    print(cache_info)
    
    return recommendations[:20]
