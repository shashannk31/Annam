from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    CUISINE_CHOICES = [
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
    ]
    cuisine_type = forms.ChoiceField(choices=CUISINE_CHOICES, widget=forms.RadioSelect)

    STATES_CHOICES = [
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu & Kashmir', 'Jammu & Kashmir')
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Ladakh', 'Ladakh')
        ('Lakshadweep', 'Lakshadweep'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]
    state = forms.ChoiceField(choices=STATES_CHOICES, widget=forms.Select)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'organization_type', 'organization_name', 'cuisine_type', 'phone', 'city', 'state', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput()
        self.fields['password2'].widget = forms.PasswordInput()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
