# Generated by Django 4.1.10 on 2023-12-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_foodorder_order_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='restaurant_order_status',
            field=models.CharField(default='Nil', max_length=20),
        ),
    ]