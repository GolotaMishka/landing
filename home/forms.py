from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):
    name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    level = forms.CharField(required=False)
    place = forms.CharField(required=False)
    
    class Meta:
        model = Subscriber
        exclude = [""]