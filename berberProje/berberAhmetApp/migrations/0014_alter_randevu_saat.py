# Generated by Django 4.2.3 on 2023-10-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0013_alter_count_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randevu',
            name='saat',
            field=models.ManyToManyField(to='berberAhmetApp.randevusaatleri', verbose_name='Saat'),
        ),
    ]
