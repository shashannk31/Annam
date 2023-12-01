from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'organization_type', 'organization_name', 'cuisine_type', 'phone', 'city', 'state', 'address']

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
