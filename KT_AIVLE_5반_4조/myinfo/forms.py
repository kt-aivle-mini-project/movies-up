from django import forms
from .models import UserTable
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserTable

        fields = ['user_id', 'password', 'user_name']