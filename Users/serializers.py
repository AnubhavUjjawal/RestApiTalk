from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ApiUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ApiUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ApiUser
        fields = '__all__'