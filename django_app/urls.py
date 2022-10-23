from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('index/', views.home),
]
