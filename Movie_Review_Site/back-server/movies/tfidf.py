import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
dir_path = os.path.dirname(os.path.abspath(__file__))

# 영화 데이터 파일 경로
movie_data_file = os.path.join(dir_path, "fixtures/movie_data.json")

def calculate_tfidf(keyword):
    # JSON 파일 불러오기
    with open(movie_data_file, "r", encoding='utf-8') as json_file:
        movie_data = json.load(json_file)

    # TF-IDF 벡터화
    corpus = [movie['fields']['overview'] for movie in movie_data]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # 입력값에 대한 TF-IDF 벡터 계산
    input_tfidf = vectorizer.transform([keyword])

    # 코사인 유사도 계산
    similarity_scores = cosine_similarity(input_tfidf, tfidf_matrix)

    # 추천 영화 목록 생성
    recommendations = []

    # 유사도가 높은 순으로 추천 영화 선정
    similar_indices = similarity_scores.argsort().flatten()[::-1]
    for idx in similar_indices:
        recommendations.append(movie_data[idx])

    return recommendations
