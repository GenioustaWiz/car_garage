# Generated by Django 4.0.10 on 2023-09-30 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors_counter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='day',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='minute',
        ),
    ]
