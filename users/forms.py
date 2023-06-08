from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile, BillingAdress
from phone_field import PhoneField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required= True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=80)
    dob = forms.DateField()


class UpdateProfile(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta : 
        model = Profile
        fields = ['phone', 'image']


class UpdateUser(forms.ModelForm):   

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']


class BillingModelForm(forms.ModelForm):
    class Meta:
        model = BillingAdress
        fields = '__all__'
        exclude = ['user']

