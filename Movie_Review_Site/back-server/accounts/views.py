from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, ProfileSerializer, WishSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User
from movies.models import Movie

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 프로필 조회
def profile(request, username):
    if request.method == 'GET':
        person = get_object_or_404(get_user_model(), username=username)
        serializer = ProfileSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
# 팔로우
def follow(request, username):
    if request.method == 'POST':
        target_user = User.objects.get(username=username)
        follower = request.user

        # 자기 자신 팔로우 한 경우
        if follower == target_user:
            return Response({"error": "자기 자신은 팔로우 할 수 없습니다ㅠ"}, status=status.HTTP_400_BAD_REQUEST)

        if follower.followings.filter(username=target_user.username).exists():
            # 이미 팔로우 중인 경우, 팔로우 해제
            follower.followings.remove(target_user)
            is_followed = False
        else:
            # 팔로우 추가
            follower.followings.add(target_user)
            is_followed = True

        context = {
            'is_followed': is_followed,
            'followers_count': target_user.followers.count(),
            'followings_count': target_user.followings.count(),
        }
        return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# 위시리스트
def user_wishlist(request, username):
    # 유저가 찜한 영화 목록을 보여준다.
    if request.method == 'GET':
        target_user = User.objects.get(username=username)
        wishlist = target_user.wishlist.all()
        print(wishlist)
        # 위시리스트에 영화가 있으면 반환
        if wishlist.exists():
            serializer = WishSerializer(wishlist, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message' : '아직 위시리스트가 없습니다. 영화를 찜해보세요!'})
    