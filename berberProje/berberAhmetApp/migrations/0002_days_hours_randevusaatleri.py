# Generated by Django 4.2.3 on 2023-10-11 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('günler', models.CharField(max_length=10, verbose_name='Günler')),
            ],
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saatler', models.CharField(max_length=10, verbose_name='Saatler')),
            ],
        ),
        migrations.CreateModel(
            name='RandevuSaatleri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berberAhmetApp.days', verbose_name='Gün')),
                ('saat', models.ManyToManyField(to='berberAhmetApp.hours', verbose_name='Saat')),
            ],
        ),
    ]
