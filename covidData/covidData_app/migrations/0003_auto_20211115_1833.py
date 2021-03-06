# Generated by Django 3.2.9 on 2021-11-15 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('covidData_app', '0002_auto_20211115_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='lastChange',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='lastUpdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
