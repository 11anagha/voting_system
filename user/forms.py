from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField(max_length=100)
    voterId = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ["username", "full_name", "address", "age", "voterId", "password1", "password2"]