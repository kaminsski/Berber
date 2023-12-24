# Generated by Django 4.2.6 on 2023-10-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0030_alter_appuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tatil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('tatil', models.ManyToManyField(to='berberAhmetApp.days', verbose_name='Tatil günleri')),
            ],
        ),
    ]