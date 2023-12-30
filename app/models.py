from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    organization_type = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    cuisine_type = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.TextField()
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    def __str__(self):
        return self.username

class FoodOrder(models.Model):
    id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255)
    cuisine_type = models.CharField(max_length=20)
    restaurant_phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    restaurant_address = models.TextField()
    charity_name = models.CharField(max_length=255, default="Nil")
    delivery_address = models.TextField()
    charity_phone = models.CharField(max_length=15)
    time_of_preparation = models.DateTimeField()
    name_of_food = models.CharField(max_length=255)
    food_cuisine = models.CharField(max_length=20)
    quantity_serves = models.IntegerField()
    storage_duration = models.CharField(max_length=100)
    tentative_collection_time = models.DateTimeField()
    packing_present = models.CharField(max_length=3)
    is_live = models.BooleanField(default=False)
    collected_time = models.DateTimeField(null=True, blank=True)
    restaurant_inbox = models.BooleanField(default=False) #to be displayed in restaurant inbox
    charity_inbox = models.BooleanField(default=False) #to be displayed in charity inbox
    display_status = models.BooleanField(default=False) #to be displayed on contributions/order history
    accept_reject_status = models.BooleanField(default=True) #for making the accept/reject button vanish after clicking
    order_timestamp = models.DateTimeField(auto_now_add=True) #time when order was placed
    restaurant_order_status = models.CharField(max_length=20, default="Nil")
    #restaurant_notification = models.BooleanField(default=True)
