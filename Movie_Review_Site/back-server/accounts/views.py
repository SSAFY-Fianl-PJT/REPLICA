from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, ProfileSerializer, FollowSerializer, WishSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    if request.method == 'GET':
        person = get_object_or_404(get_user_model(), username=username)
        serializer = ProfileSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    if request.method == 'POST':
        target_user = User.objects.get(username=username)

        if request.user == target_user:
            return Response({"error": "자기 자신은 팔로우 할 수 없습니다ㅠ"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FollowSerializer(data={'follower': request.user.username, 'following': target_user.username})
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "사용자를 팔로우하였습니다."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wishlist(request, username):
    # 유저가 찜한 영화 목록을 보여준다.
    if request.method == 'GET':
        target_user = User.objects.get(username=username)
        wishlist = target_user.wishlist.all()
        if wishlist.exists():
            serializer = WishSerializer(wishlist, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message' : '아직 위시리스트가 없습니다. 영화를 찜해보세요!'})
    