# Generated by Django 4.2.3 on 2023-10-13 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0011_remove_randevu_dolu_mu_hours_dolu_mu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='randevu',
            old_name='sira',
            new_name='siras',
        ),
    ]
