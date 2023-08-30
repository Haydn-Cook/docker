from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

name = 'login'
urlpatterns = [
    path('', views.login, name='login'),
    path('login_create/', views.login_create, name = 'login_create'),
    path('create_user/', views.create_user, name='create_user'),
    path('login_user/', auth_views.LoginView.as_view(),name = 'login_user')
]