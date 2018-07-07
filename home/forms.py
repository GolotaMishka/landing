from django import forms
from .models import *


class SubscriberFaceToFaceForm(forms.ModelForm):
    name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    place = forms.CharField(required=False)
    
    class Meta:
        model = FaceToFace
        exclude = [""]


class SubscriberGroupForm(forms.ModelForm):
    name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    level = forms.CharField(required=False)

    class Meta:
        model = Group
        exclude = [""]