# Generated by Django 5.2.4 on 2025-07-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Phone number"
            ),
        ),
    ]
