from django.urls import path, include
from rest_framework.routers import DefaultRouter
from giangvien.views import GiangVienCreateAPIView, GiangVienDetail


urlpatterns = [
  path('create', GiangVienCreateAPIView.as_view()),
  path('<int:pk>',GiangVienDetail.as_view() ),
]