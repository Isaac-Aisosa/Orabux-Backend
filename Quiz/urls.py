from django.urls import path
from . import views

urlpatterns = [
        path('api-save-quiz-from1/', views.save_quiz_form1),
        path('api-save-quiz-from2/photo/', views.save_quiz_form2_photo),
        path('api-save-quiz-from3/', views.save_quiz_form3),
        path('api-quiz-preview/', views.get_quiz_details),
        path('api-quiz-payment/success/', views.quiz_payment_success),
]
