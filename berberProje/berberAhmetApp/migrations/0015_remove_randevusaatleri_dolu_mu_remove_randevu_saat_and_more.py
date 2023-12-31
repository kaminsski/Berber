# Generated by Django 4.2.3 on 2023-10-14 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('berberAhmetApp', '0014_alter_randevu_saat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randevusaatleri',
            name='dolu_mu',
        ),
        migrations.RemoveField(
            model_name='randevu',
            name='saat',
        ),
        migrations.AlterField(
            model_name='randevusaatleri',
            name='saat',
            field=models.ManyToManyField(null=True, to='berberAhmetApp.hours', verbose_name='Saat'),
        ),
        migrations.AddField(
            model_name='randevu',
            name='saat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='berberAhmetApp.randevusaatleri', verbose_name='miras'),
        ),
    ]
