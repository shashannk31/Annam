# Generated by Django 4.1.10 on 2023-11-05 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]