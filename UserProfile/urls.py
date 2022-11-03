from django.urls import path
from . import views
from .views import AuthToken

urlpatterns = [
    path("api-email-check/", views.Email_check.as_view()),
    path("api-username-check/", views.Username_check.as_view()),
    path("api-user-signup/", views.UserCreate.as_view()),
    path('api-user-login/', AuthToken.as_view()),
    path('api-get-user-profile/', views.get_user_profile),
    path('api-update-user-profile/', views.update_user_profile),
    path('api-update-user-profile/image/', views.update_user_profile_image),
]

