from django.urls import path
from . import views

urlpatterns = [

       path('api-user-post/', views.user_post),
       path('api-get-user-post/', views.get_user_post),

]
