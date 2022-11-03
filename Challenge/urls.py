from django.urls import path
from . import views

urlpatterns = [
       path('api-save-challenge-from1/', views.save_challenge_form1),
       path('api-save-challenge-from2/photo/', views.save_challenge_form2_photo),
       path('api-save-challenge-from2/audio/', views.save_challenge_form2_audio),
       path('api-save-challenge-from2/video/', views.save_challenge_form2_video),
       path('api-save-challenge-from3/', views.save_challenge_form3),
       path('api-save-challenge-from4/reward/', views.save_challenge_form4_reward),


       path('api-get-min-vote/', views.get_minimum_vote),
       path('api-get-challenge/details/', views.get_challenge_details),
       path('api-get-challenge/payment/success/', views.challenge_payment_success),

       path('api-get-user/created/contest/', views.get_user_created_contest),
]
