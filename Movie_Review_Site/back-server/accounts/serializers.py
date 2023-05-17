from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname', '')
        user.save()

class ProfileSerializer(serializers.ModelSerializer):
    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nickname', 'wishlist', 'date_joined', 'following_count', 'followers_count', )
    def get_followings_count(self, obj):
        return obj.followings.count()

    def get_followers_count(self, obj):
        return obj.followers.count()
    

class WishSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'
