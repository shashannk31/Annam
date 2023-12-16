from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FoodOrder

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'organization_type', 'organization_name',
    'cuisine_type', 'phone', 'city', 'state', 'address']

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_name', 'cuisine_type', 'restaurant_phone',
    'city', 'state', 'restaurant_address', 'delivery_address', 'charity_phone',
    'time_of_preparation', 'name_of_food', 'food_cuisine', 'quantity_serves',
    'storage_duration', 'tentative_collection_time', 'packing_present', 'is_live',
    'collected_time')
    search_fields = ('organization_name', 'cuisine_type', 'city', 'state')
    list_filter = ('is_live', 'collected_time')

admin.site.register(CustomUser, CustomUserAdmin)
