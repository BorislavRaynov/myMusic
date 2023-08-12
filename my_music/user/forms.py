from django import forms
from .models import User


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'})
        }
