# Generated by Django 4.2.6 on 2023-12-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0037_alter_appuser_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Şifre'),
        ),
    ]
