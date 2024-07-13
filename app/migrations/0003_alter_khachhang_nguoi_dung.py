# Generated by Django 5.0.6 on 2024-06-23 04:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_sanpham_hinh_anh'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='khachhang',
            name='nguoi_dung',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='khachhang', to=settings.AUTH_USER_MODEL),
        ),
    ]
