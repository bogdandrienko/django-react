from django.contrib import admin
from django.urls import path, re_path, include
from django_api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('index/', views.home),

    path('token/', TokenObtainPairView.as_view()),
    # "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
    # .eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2NTMxMjQzLCJpYXQiOjE2NjY1MzAzNDMsImp0aSI6ImFmMTRkMjdhNWYwNTQ0MDNhY2QwZTg2ZDEyOThiYjNiIiwidXNlcl9pZCI6MX0.8tV4echQvstfTHJthn1KZAY0gga9hYTbHmevHXWTEeI"
    path('token/refresh/', TokenRefreshView.as_view()),

    re_path(r'^get_all_active_users/$', views.get_all_active_users),
    re_path(r'^register/$', views.register),

    # GET "read idea list": "http://127.0.0.1:8000/api/idea/?search=all&sort=name&page=1&limit=10"
    # POST "create idea": "http://127.0.0.1:8000/api/idea/"
    # re_path(r'^idea/$', backend_views.api_idea, name='api_idea'),

    # GET (read idea) 'http://127.0.0.1:8000/api/idea/1/'
    # PUT (update idea) 'http://127.0.0.1:8000/api/idea/1/'
    # DELETE (delete idea) 'http://127.0.0.1:8000/api/idea/1/'
    # re_path(r'^api/idea/(?P<idea_id>\d+)/$', backend_views.api_idea_id, name='api_idea_id'),
]
