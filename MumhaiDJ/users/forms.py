from django.forms import ModelForm, widgets
from .models import Customer
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model =  Customer
        fields = ['user_type','first_name', 'last_name', 'number', 'gender', 'econ_name', 'econ_num']
        widgets = {
            'gender':widgets.RadioSelect(),
            'number':widgets.NumberInput(attrs={'max_length':10}),
            'econ_num':widgets.NumberInput(attrs={'max_length':10})
        }
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields= ['user_type','first_name', 'last_name', 'number', 'gender', 'econ_name', 'econ_num']

        
#try forms.Form to allow for more form widget control