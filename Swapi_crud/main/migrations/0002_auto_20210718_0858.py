# Generated by Django 3.2.5 on 2021-07-18 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='Films',
        ),
        migrations.RemoveField(
            model_name='people',
            name='Homeworld',
        ),
        migrations.RemoveField(
            model_name='people',
            name='Species',
        ),
        migrations.RemoveField(
            model_name='people',
            name='Starships',
        ),
        migrations.RemoveField(
            model_name='people',
            name='URL',
        ),
        migrations.RemoveField(
            model_name='people',
            name='Vehicles',
        ),
    ]
