# Generated by Django 4.2.6 on 2023-12-20 16:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0036_iptalinfo_tarih'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='TR'),
        ),
    ]
