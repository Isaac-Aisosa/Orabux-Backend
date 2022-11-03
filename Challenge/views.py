from datetime import datetime

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
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

from .models import *
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
def save_challenge_form1(request):
    title = request.data['title']
    types = request.data['type']
    description = request.data['description']
    challenge = Challenge()
    challenge.user = request.user
    challenge.title = title
    challenge.type = types
    challenge.description = description
    challenge.draft = True
    challenge.save()
    pk = challenge.pk
    return Response({'pk': pk, 'title': challenge.title, })


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_challenge_form2_photo(request):
    photo = request.FILES['photo']
    pk = request.data['pk']
    challenge = Challenge.objects.get(pk=pk)
    challenge.attachImage = photo
    challenge.save()
    return Response(status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_challenge_form2_audio(request):
    audio = request.FILES['audio']
    pk = request.data['pk']
    challenge = Challenge.objects.get(pk=pk)
    challenge.attachAudio = audio
    challenge.save()
    return Response(status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_challenge_form2_video(request):
    video = request.FILES['video']
    pk = request.data['pk']
    challenge = Challenge.objects.get(pk=pk)
    challenge.attachVideo = video
    challenge.save()
    return Response(status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_challenge_form3(request):
    pk = request.data['pk']
    allowed_voter = request.data['allowed_voter']
    minVote = request.data['minVote']
    #  start_date = request.POST['start_date']
    # end_date = request.data['end_date']
    duration = request.data['duration']
    challenge = Challenge.objects.get(pk=pk)
    challenge.voter = allowed_voter
    challenge.minimumVote = minVote
    # challenge.start_date = start_date
    # challenge.end_date = end_date
    # print(start_date)
    # print(end_date)
    challenge.duration = duration
    challenge.save()
    return Response(status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_challenge_form4_reward(request):
    pk = request.data['pk']
    cash = request.data['cash']
    physicalReward = request.data['physicalReward']
    number_winner = request.data['number_winner']
    worth = request.data['worth']
    other_benefit = request.data['otherBenefit']
    reward_1 = request.data['reward_1']
    reward_2 = request.data['reward_2']
    reward_3 = request.data['reward_3']
    reward_4 = request.data['reward_4']
    reward_5 = request.data['reward_5']
    reward_6 = request.data['reward_6']
    reward_7 = request.data['reward_7']
    reward_8 = request.data['reward_8']
    reward_9 = request.data['reward_9']
    reward_10 = request.data['reward_10']
    challenge = Challenge.objects.get(pk=pk)
    challenge.cashReward = True
    challenge.physicalReward = False
    challenge.select_winner = number_winner
    challenge.worth = worth
    challenge.otherReward = other_benefit
    challenge.first_place_reward = reward_1
    challenge.second_place_reward = reward_2
    challenge.third_place_reward = reward_3
    challenge.forth_place_reward = reward_4
    challenge.firth_place_reward = reward_5
    challenge.six_place_reward = reward_6
    challenge.seven_place_reward = reward_7
    challenge.eight_place_reward = reward_8
    challenge.ninth_place_reward = reward_9
    challenge.tenth_place_reward = reward_10
    challenge.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_minimum_vote(request):
    minVote = ChallengeMinimumVote.objects.get(active=True)
    return Response({
        'minVote': minVote.value,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_challenge_details(request):
    pk = request.data['pk']
    challenge = Challenge.objects.get(pk=pk)
    print(challenge.user)
    if challenge.attachImage:
        image = challenge.attachImage.url
    else:
        image = ''

    if challenge.attachVideo:
        video = challenge.attachVideo.url
    else:
        video = ''

    if challenge.attachAudio:
        audio = challenge.attachAudio.url
    else:
        audio = ''

    return Response({
        'user': challenge.user.username,
        'title': challenge.title,
        'description': challenge.description,
        'category': challenge.type,
        'attach_image': image,
        'attach_video': video,
        'attach_audio': audio,
        'allowed_voter': challenge.voter,
        'minimumVote': challenge.minimumVote,
        'start_date': challenge.start_date,
        'end_date': challenge.end_date,
        'duration': challenge.duration,
        'select_winner': challenge.select_winner,
        'cashReward': challenge.cashReward,
        'physicalReward': challenge.physicalReward,
        'first_place_reward': challenge.first_place_reward,
        'second_place_reward': challenge.second_place_reward,
        'third_place_reward': challenge.third_place_reward,
        'forth_place_reward': challenge.forth_place_reward,
        'firth_place_reward': challenge.firth_place_reward,
        'six_place_reward': challenge.six_place_reward,
        'seven_place_reward': challenge.seven_place_reward,
        'eight_place_reward': challenge.eight_place_reward,
        'ninth_place_reward': challenge.ninth_place_reward,
        'tenth_place_reward': challenge.tenth_place_reward,
        'worth': challenge.worth,
        'approved': challenge.approved,
        'rejected': challenge.rejected,
        'draft': challenge.draft,
        'pending': challenge.pending,
        'active': challenge.active,
        'closed': challenge.closed,
        'payin': challenge.payin,
        'payout': challenge.payout,
        'payoutFailed': challenge.payoutFailed,
        'payinFailed': challenge.payinFailed,
    })


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def challenge_payment_success(request):
    pk = request.data['pk']
    challenge = Challenge.objects.get(pk=pk)
    challenge.payin = True
    challenge.approved = True
    challenge.active = True
    challenge.draft = False
    challenge.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_created_contest(request):
    challenge = Challenge.objects.filter(user=request.user).order_by('-timestamp').values()

    contest = challenge
    return Response({
        'contest': list(challenge),
        'count': contest.count()
    })
