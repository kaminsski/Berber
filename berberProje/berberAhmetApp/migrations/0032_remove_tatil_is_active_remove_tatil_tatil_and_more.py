# Generated by Django 4.2.6 on 2023-10-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0031_tatil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tatil',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='tatil',
            name='tatil',
        ),
        migrations.AddField(
            model_name='tatil',
            name='tatil',
            field=models.DateField(null=True, verbose_name='Tatil'),
        ),
    ]
