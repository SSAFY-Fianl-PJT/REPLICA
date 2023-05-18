from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from movies.serializers import MovieDetailSerializer
from .models import User
from django.contrib.auth import get_user_model

# 회원가입 폼
class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname', '')
        user.save()

# 프로필
class ProfileSerializer(serializers.ModelSerializer):
    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    wishlist = MovieDetailSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nickname', 'wishlist', 'date_joined', 'followings_count', 'followers_count', )

    def get_followings_count(self, obj):
        return obj.followings.count()

    def get_followers_count(self, obj):
        return obj.followers.count()
    
# 팔로우
class FollowSerializer(serializers.Serializer):
    follower = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model().objects.all())
    following = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model().objects.all())

    def create(self, validated_data):
        follower = validated_data['follower']
        following = validated_data['following']
        follower.followings.add(following)
        return follower

# 위시리스트
class WishSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('wishlist', )
