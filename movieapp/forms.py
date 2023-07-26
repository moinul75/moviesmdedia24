from django import forms 
from .models import Registration


class SignupForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        
        
# class Login(forms.ModelForm):
#     class Meta:
#         model = Registration
#         fields = ['email','']
        