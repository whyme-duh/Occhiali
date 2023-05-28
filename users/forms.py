from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required= True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=80)
    dob = forms.DateField()
