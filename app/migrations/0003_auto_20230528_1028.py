# Generated by Django 3.1.14 on 2023-05-28 01:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了時間'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='開始時間'),
        ),
    ]
