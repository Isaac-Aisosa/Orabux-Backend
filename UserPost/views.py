from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import NotAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User
from rest_framework import status
from django.http import Http404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_post(request):
    files = request.FILES['post_file']
    caption = request.data['caption']
    file_type = request.data['type']
    post = Post()
    post.user = request.user
    post.file = files
    post.type = file_type
    post.caption = caption
    post.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_post(request):
    posts = Post.objects.filter(user=request.user).order_by('-timestamp').values()

    return Response({
        'posts': list(posts),
        'posts_count': posts.count()
    })
