# Generated by Django 4.2.3 on 2023-10-14 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0018_rename_saat_randevu_r_rs_rename_siras_randevu_r_sayi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randevu',
            name='r_rs',
        ),
        migrations.RemoveField(
            model_name='randevu',
            name='r_sayi',
        ),
    ]
