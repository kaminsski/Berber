# Generated by Django 4.2.3 on 2023-10-11 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0002_days_hours_randevusaatleri'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randevusaatleri',
            name='day',
        ),
    ]
