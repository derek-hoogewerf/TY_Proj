from django.forms import ModelForm, widgets
from .models import Site_Feedback
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SiteFeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = Site_Feedback
        fields = ['reviewee','title','content','rating','report']
        success_url = ''
        widgets = {
            #'date' : widgets.DateInput(attrs={'type': 'date'}),
            #'customer' : widgets.HiddenInput(),
            #'employee' : widgets.HiddenInput(),
            #'status' : widgets.HiddenInput(),
        }