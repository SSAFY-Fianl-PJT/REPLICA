from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Review, Comment
from movies.models import Movie
# from django.http import JsonResponse
from .serializers import ReviewSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # 리뷰 생성
    elif request.method == 'POST':
        movie_title = request.data.get('movie_title')
        try:
            movie = Movie.objects.get(title=movie_title)
        except Movie.DoesNotExist:
            return Response({'message': '영화를 찾을 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user, movie = movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            return Response(
            {'message': '게시글이 삭제되었습니다.'},
            status=status.HTTP_204_NO_CONTENT
        )
        else:
            return Response(
                {'message': '게시글은 작성자만 삭제할 수 있습니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )
    elif request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'message': '게시글은 작성자만 수정할 수 있습니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comments(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'GET':
        comments = review.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
                serializer.save(review = review, comment_user = request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_update(request, review_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.comment_user:
        return Response(
            {'message': '댓글은 작성자만 수정/삭제할 수 있습니다.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    else:

        if request.method == 'DELETE':
            comment.delete()
            return Response(
            {'message': '댓글이 삭제되었습니다.'},
            status=status.HTTP_204_NO_CONTENT
            )

        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)