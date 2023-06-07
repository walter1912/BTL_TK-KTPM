from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import SinhVien
from .serializers import SinhVienSerializer

class SinhVienCreateAPIView(CreateAPIView):
    serializer_class = SinhVienSerializer
    def post(self, request, *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'ma_sv': request.data.get('ma_sv'),
            'ten_sv': request.data.get('ten_sv'),
            'email': request.data.get('email'),
            'dob': request.data.get('dob'),
            'address': request.data.get('address'),
            'gv_id': request.data.get('gv_id'),
        }
        serializer = SinhVienSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SinhVienDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer