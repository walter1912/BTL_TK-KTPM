from django.urls import path
from .views import(
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetail
)
urlpatterns = [
    path('register',UserCreateAPIView.as_view(), name='register'),
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('<int:pk>', UserDetail.as_view(), name='user-list'),
]