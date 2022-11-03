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

from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User
from rest_framework import status
from django.http import Http404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer


# Create your views here.
class Email_check(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        users = User.objects.filter(email=email)
        if users.exists():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_200_OK)


# check username if exist
class Username_check(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        users = User.objects.filter(username=username)
        if users.exists():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_200_OK)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class AuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    profile = UserProfile.objects.get(user=request.user.pk)
    user = User.objects.get(user=request.user.pk)
    profileImage = profile.profileImage.url
    print(profileImage)
    return Response({
        'username': user.username,
        'email': user.email,
        'name': profile.name,
        'bio': profile.bio,
        'profession': profile.profession,
        'location': profile.location,
        'DOB': profile.DOB,
        'Gender': profile.Gender,
        'phone': profile.Phone,
        'followers': profile.follower.count(),
        'following': profile.following.count(),
        'joined': profile.joined,
        'profileImage': profileImage,
    })


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    username = request.data['username']
    name = request.data['name']
    bio = request.data['bio']
    DOB = request.data['DOB']
    profession = request.data['profession']
    phone = request.data['phone']
    location = request.data['location']
    update_username = User.objects.get(user=request.user.pk)
    update_username.username = username
    update_username.save()

    profile = UserProfile.objects.get(user=request.user.pk)
    profile.name = name
    profile.bio = bio
    profile.DOB = DOB
    profile.Phone = phone
    profile.profession = profession
    profile.location = location
    profile.save()
    return Response(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_profile_image(request):
    profileImage = request.FILES['profileImage']
    profile = UserProfile.objects.get(user=request.user.pk)
    profile.profileImage = profileImage
    profile.save()
    return Response({
        'profileImage': profile.profileImage.url,
    })
