# Generated by Django 4.1.10 on 2023-11-11 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_userprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
    ]
