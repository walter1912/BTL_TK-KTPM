from rest_framework import serializers
from .models import User
from rest_framework import serializers
from .models import User

# from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
