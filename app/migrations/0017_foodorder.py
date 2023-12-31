# Generated by Django 4.1.10 on 2023-12-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_customuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255)),
                ('cuisine_type', models.CharField(max_length=20)),
                ('restaurant_phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('restaurant_address', models.TextField()),
                ('delivery_address', models.TextField()),
                ('charity_phone', models.CharField(max_length=15)),
                ('time_of_preparation', models.DateTimeField()),
                ('name_of_food', models.CharField(max_length=255)),
                ('food_cuisine', models.CharField(max_length=20)),
                ('quantity_serves', models.IntegerField()),
                ('storage_duration', models.CharField(max_length=100)),
                ('tentative_collection_time', models.DateTimeField()),
                ('packing_present', models.BooleanField(default=False)),
                ('is_live', models.BooleanField(default=False)),
                ('collected_time', models.DateTimeField()),
            ],
        ),
    ]
