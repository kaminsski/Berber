# Generated by Django 4.2.3 on 2023-10-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0027_randevu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randevu',
            name='description',
            field=models.CharField(default=' ', max_length=30, verbose_name='Açıklama'),
        ),
    ]
