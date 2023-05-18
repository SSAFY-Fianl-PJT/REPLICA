from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie

# 댓글
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'comment_user', )


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    # 영화 제목, 해당 리뷰의 댓글들 가져오기
    movie_title =serializers.CharField()
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', )

