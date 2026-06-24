from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView


class CreateList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        if not posts:
            raise ValidationError({
                'msg': 'Post not found!',
                'status': status.HTTP_204_NO_CONTENT
            })
        serializer = PostSerializer(posts, many=True)
        
        return Response({
            'msg': 'List Porduct!',
            'status': status.HTTP_200_OK,
            'posts': serializer.data
        })
        
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'msg': "Created",
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })
        

class DetailUpdateDelete(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if not post:
            raise ValidationError({
                'msg': "Post not found!",
                'status': status.HTTP_204_NO_CONTENT
            })
        serializer = PostSerializer(post)
        
        return Response({
            'msg': "Post Detail",
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })
        
        