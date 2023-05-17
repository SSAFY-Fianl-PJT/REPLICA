from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)

    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname', '')
        user.save()
