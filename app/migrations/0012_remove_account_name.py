# Generated by Django 4.1.10 on 2023-11-26 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_account_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
    ]
