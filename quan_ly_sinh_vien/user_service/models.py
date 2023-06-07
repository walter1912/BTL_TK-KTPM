from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, blank = False)
    confirm_password = models.CharField(max_length=20, blank = False)
    role = models.IntegerField(max_length=10)
    # role = 1 cho giangvien 
    # role = 2 cho sinhvien
    def __str__(self):
        return self.username
