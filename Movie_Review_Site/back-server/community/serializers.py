
from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model

# 댓글
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'comment_user', )


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    # 영화 제목, 해당 리뷰의 댓글들 가져오기
    movie_title = serializers.CharField()
    comments = CommentSerializer(many=True, required=False)
    likes_count = serializers.SerializerMethodField()
    likes = serializers.PrimaryKeyRelatedField(many=True, queryset=get_user_model().objects.all(), required=False)
    username = serializers.CharField(required=False)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'username', )

    def get_likes_count(self, obj):
        return obj.likes.count()