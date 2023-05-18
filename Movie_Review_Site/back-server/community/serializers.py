
from rest_framework import serializers
from .models import Review, Comment

# 댓글
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'comment_user', )


# # 리뷰 좋아요
# class ReviewLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('likes',)


# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    # 영화 제목, 해당 리뷰의 댓글들 가져오기
    movie_title =serializers.CharField()
    comments = CommentSerializer(many=True)
    likes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', )

    def get_likes_count(self, obj):
        return obj.likes.count()

