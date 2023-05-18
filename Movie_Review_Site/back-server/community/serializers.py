from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'comment_user', )

        
class ReviewSerializer(serializers.ModelSerializer):
    movie_title =serializers.CharField()
    comments = CommentSerializer(many=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', )

