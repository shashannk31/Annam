# Generated by Django 4.1.10 on 2023-12-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_foodorder_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='charity_inbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='foodorder',
            name='restaurant_inbox',
            field=models.BooleanField(default=False),
        ),
    ]
