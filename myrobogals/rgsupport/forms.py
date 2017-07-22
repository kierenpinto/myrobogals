from django import forms
from .models import Request, Department

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['enquiry_type','name','email','chapter','message',]

class RequestForm_Edit(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['enquiry_type','name','email','chapter','message','date','resolved',]

class Issue_List_Filter(forms.Form):
    blank_choice = (None,'-----')

    forms_choices_fields = [blank_choice,('unresolved','unresolved'),('resolved','resolved')]
    enquiry_status = forms.ChoiceField(choices=forms_choices_fields, required = False)

    dept_fields = [blank_choice] + [(str(field),str(field)) for field in Department.objects.all()]
    enquiry_type = forms.ChoiceField(choices=dept_fields, required=False, initial={'value':'----'})

    date_order = forms.ChoiceField(choices = ((blank_choice),('Ascending','Oldest'),('Descending','Newest')), required=False)
    search = forms.CharField(max_length=50, required=False, initial={'value':'Search'})