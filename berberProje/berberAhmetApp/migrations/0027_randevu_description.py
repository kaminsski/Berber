# Generated by Django 4.2.3 on 2023-10-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0026_alter_appuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='randevu',
            name='description',
            field=models.CharField(default='Admin', max_length=30, verbose_name='Açıklama'),
        ),
    ]