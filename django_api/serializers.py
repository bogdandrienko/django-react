from django.contrib.auth.models import User
from rest_framework import serializers


class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # ['room_number', 'date']
