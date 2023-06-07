from django.urls import include, path
from rest_framework import routers
from sinhvien.views import SinhVienCreateAPIView, SinhVienDetail

urlpatterns = [
    path('create', SinhVienCreateAPIView.as_view()),
    path('<int:pk>', SinhVienDetail.as_view()),
]




