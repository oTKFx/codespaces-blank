from django.urls import path
from . import views
from .views import create_user



urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('signup', views.welcome, name="signup"),
    path('login', views.welcome, name="signin"),
    path('create_user/', create_user, name='create_user'),
]