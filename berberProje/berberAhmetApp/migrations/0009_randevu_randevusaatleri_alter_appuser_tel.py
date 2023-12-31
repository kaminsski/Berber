# Generated by Django 4.2.3 on 2023-10-13 00:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0008_remove_appuser_about_appuser_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='randevu',
            name='randevuSaatleri',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='berberAhmetApp.randevusaatleri', verbose_name='randevuSaatleri'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='TR'),
        ),
    ]
