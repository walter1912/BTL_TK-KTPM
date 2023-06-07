from django.db import models
# Create your models here.
class SinhVien(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    ma_sv = models.CharField(max_length=20)
    ten_sv = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    dob = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    gv_id = models.IntegerField(max_length=100)
    
    def __str__(self):
        return self.username
