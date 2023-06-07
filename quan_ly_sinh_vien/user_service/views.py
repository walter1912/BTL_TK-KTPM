from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from .models import User 

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
            'confirm_password': request.data.get('confirm_password'),
            'role': request.data.get('role')
        }
        if data['confirm_password']!=data['password'] :
            return Response("error confirm_password", status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = {
            'username' : request.data.get('username'),
            'password' : request.data.get('password')

        }
        user = User.objects.filter(username=data['username'], password = data['password']).first()
        if user is not None:
            return Response('ok', status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer