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
def save_quiz_form1(request):
    title = request.data['title']
    numberQuestion = request.data['numberQuestion']
    question1 = request.data['question1']
    answer1 = request.data['answer1']
    question2 = request.data['question2']
    answer2 = request.data['answer2']
    question3 = request.data['question3']
    answer3 = request.data['answer3']
    question4 = request.data['question4']
    answer4 = request.data['answer4']
    question5 = request.data['question5']
    answer5 = request.data['answer5']
    quiz = Quiz()
    quiz.user = request.user
    quiz.title = title
    quiz.numberQuestions = numberQuestion
    quiz.question1 = question1
    quiz.answer1 = answer1
    quiz.question2 = question2
    quiz.answer2 = answer2
    quiz.question3 = question3
    quiz.answer3 = answer3
    quiz.question4 = question4
    quiz.answer4 = answer4
    quiz.question5 = question5
    quiz.answer5 = answer5
    quiz.draft = True
    quiz.save()
    pk = quiz.pk
    return Response({'pk': pk, 'title': quiz.title, })


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_quiz_form2_photo(request):
    photo = request.FILES['photo']
    pk = request.data['pk']
    quiz = Quiz.objects.get(pk=pk)
    quiz.attachImage = photo
    quiz.save()
    return Response(status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_quiz_form3(request):
    pk = request.data['pk']
    #  start_date = request.POST['start_date']
    # end_date = request.data['end_date']
    duration = request.data['duration']
    cash = request.data['cash']
    physicalReward = request.data['physicalReward']
    worth = request.data['worth']
    other_benefit = request.data['otherBenefit']
    grandPrize = request.data['grandPrize']
    quiz = Quiz.objects.get(pk=pk)
    quiz.cashPrize = grandPrize
    quiz.worth = worth
    quiz.otherBenefit = other_benefit
    quiz.duration = duration
    quiz.cashReward = True
    quiz.physicalReward = False
    # challenge.start_date = start_date
    # challenge.end_date = end_date
    # print(start_date)
    # print(end_date)
    quiz.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_quiz_details(request):
    pk = request.data['pk']
    quiz = Quiz.objects.get(pk=pk)
    if quiz.attachImage:
        image = quiz.attachImage.url
    else:
        image = ''

    return Response({
        'user': quiz.user.username,
        'title': quiz.title,
        'numberQuestion': quiz.numberQuestions,
        'question1': quiz.question1,
        'answer1': quiz.answer1,
        'question2': quiz.question2,
        'answer2': quiz.answer2,
        'question3': quiz.question3,
        'answer3': quiz.answer3,
        'question4': quiz.question4,
        'answer4': quiz.answer4,
        'question5': quiz.question5,
        'answer5': quiz.answer5,
        'attach_image': image,
        'start_date': quiz.start_date,
        'end_date': quiz.end_date,
        'duration': quiz.duration,
        'cashReward': quiz.cashReward,
        'physicalReward': quiz.physicalReward,
        'grandPrize': quiz.cashPrize,
        'worth': quiz.worth,
        'approved': quiz.approved,
        'rejected': quiz.rejected,
        'draft': quiz.draft,
        'pending': quiz.pending,
        'active': quiz.active,
        'closed': quiz.closed,
        'payin': quiz.payin,
        'payout': quiz.payout,
        'payoutFailed': quiz.payoutFailed,
        'payinFailed': quiz.payinFailed,
    })


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def quiz_payment_success(request):
    pk = request.data['pk']
    quiz = Quiz.objects.get(pk=pk)
    quiz.payin = True
    quiz.approved = True
    quiz.active = True
    quiz.draft = False
    quiz.save()
    return Response(status=status.HTTP_200_OK)
