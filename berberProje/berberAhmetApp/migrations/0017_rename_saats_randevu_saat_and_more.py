# Generated by Django 4.2.3 on 2023-10-14 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0016_rename_saat_randevu_saats_alter_randevu_siras_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='randevu',
            old_name='saats',
            new_name='saat',
        ),
        migrations.RenameField(
            model_name='randevusaatleri',
            old_name='saat',
            new_name='saati',
        ),
    ]