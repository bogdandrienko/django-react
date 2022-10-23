import re

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django_api import serializers as django_serializers


# Create your views here.

def home(request):
    return render(request, 'build/index.html')


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  # @permission_classes([IsAuthenticated])
def get_all_active_users(request):
    # # users = User.objects.all()  # TODO SELECT * From user
    # # users = User.objects.get(id=1)  # TODO SELECT * From user where id = '1'
    # users = User.objects.filter(is_active=True)  # TODO SELECT * From user where is_active = '1'
    # # users - python objects
    # users_temp = []
    # for user in users:
    #     new_user = {}
    #     new_user["username"] = user.username
    #     new_user["password"] = user.password
    #     new_user["email"] = user.email
    #     new_user["is_staff"] = user.is_staff
    #     users_temp.append(new_user)
    # users = users_temp
    # # react: users - JSON
    # context = {'users': users}
    # return JsonResponse(data=context, safe=True)  # Response  - django rest framework
    users = User.objects.filter(is_active=True)
    users_serialized = django_serializers.UserCustomSerializer(instance=users, many=True).data

    users = User.objects.get(id=1)
    users = User.objects.get(username='admin')
    # users_serialized = django_serializers.UserCustomSerializer(instance=users, many=False).data
    return Response(data={"users": users_serialized, "x-total-Count": 144, "page": 5}, status=200)


@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])  # @permission_classes([IsAuthenticated])
def register(request):

    # try:
    #     email = request.data.get("email", None)
    #     password = request.data.get("password", None)
    #     if email and password:
    #         if re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password) and \
    #                 re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email):
    #             User.objects.create(
    #                 username=email,
    #                 email=email,
    #                 password=make_password(password)  # для create НУЖНО шифровать пароль, для create_user НЕТ!
    #             )
    #             return Response(status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(data={"ответ:": "Вы не прошли проверку регулярного выражения"},
    #                             status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    # except Exception as error:
    #     return Response(data=str(error), status=status.HTTP_400_BAD_REQUEST)

    try:
        print("request.POST", request.POST)
    except Exception as error:
        pass
    try:
        print("request.data", request.data)
    except Exception as error:
        pass
    try:
        print("request.FILES", request.FILES)
    except Exception as error:
        pass

    username = request.data.get('username', None)
    password = request.data["password"]

    # username = request.POST.get('username', None)
    # password = request.POST["password"]

    if username and password:
        User.objects.create(
            username=username,
            password=make_password(password)
        )
        # User.objects.create_user(
        #     username=username,
        #     password=password
        # )
        return Response(data={"response": 'successfull'}, status=201)
    return Response(data={"error": 'fail to create'}, status=404)
