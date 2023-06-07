from rest_framework import serializers
from .models import GiangVien

class GiangVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiangVien
        fields = '__all__'