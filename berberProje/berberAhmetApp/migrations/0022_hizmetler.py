# Generated by Django 4.2.3 on 2023-10-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0021_alter_count_counts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hizmetler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hizmet', models.CharField(max_length=10, verbose_name='Hizmet')),
                ('fiyat', models.CharField(max_length=10, verbose_name='Fiyat')),
                ('createdAt', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]