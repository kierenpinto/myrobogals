from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['enquiry_type','name','email','chapter','message',]

class RequestForm_Edit(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['enquiry_type','name','email','chapter','message','date','resolved',]