from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    phone = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'phone', 'password1', 'password2')
