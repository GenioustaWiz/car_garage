# Generated by Django 4.2.7 on 2023-12-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="ip_address",
            field=models.GenericIPAddressField(
                blank=True, default="0.0.0.0", null=True
            ),
        ),
    ]