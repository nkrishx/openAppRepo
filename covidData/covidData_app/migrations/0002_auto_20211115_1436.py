# Generated by Django 3.2.9 on 2021-11-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidData_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='lastChange',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
