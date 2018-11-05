from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ApiUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ApiUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ApiUser
        fields = '__all__'
   
    def create(self, validated_data):
        user_serializer = UserSerializer(data=validated_data.get("user"))
        if user_serializer.is_valid():
            user_serializer.save()
        api_user = ApiUser(user=user_serializer.instance,
                            roll_no=validated_data.get("roll_no"))
        api_user.save()
        return api_user
