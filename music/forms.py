from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

#This just stores information about the class
    class Meta: 
        model = User
        fields = ['username', 'email', 'password']
