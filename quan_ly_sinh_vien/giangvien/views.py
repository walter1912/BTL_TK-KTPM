from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import GiangVien
from .serializers import GiangVienSerializer

class GiangVienCreateAPIView(CreateAPIView):
    serializer_class = GiangVienSerializer
    def post(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'ma_gv': request.data.get('ma_gv'),
            'ten_gv': request.data.get('ten_gv'),
            'email': request.data.get('email'),
            'dob': request.data.get('dob'),
            'address': request.data.get('address'),
        }
        serializer = GiangVienSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GiangVienDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = GiangVien.objects.all()
    serializer_class = GiangVienSerializer