# Generated by Django 4.1.10 on 2023-12-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_foodorder_display_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='accept_reject_status',
            field=models.BooleanField(default=True),
        ),
    ]