# Generated by Django 4.0 on 2023-06-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('ma_sv', models.CharField(max_length=20)),
                ('ten_sv', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('gv_id', models.IntegerField(max_length=100)),
            ],
        ),
    ]
