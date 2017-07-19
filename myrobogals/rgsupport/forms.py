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
    forms_choices_fields = [('resolved','Resolved'),('unresolved','Unresolved'),]
    filters = forms.MultipleChoiceField(choices=forms_choices_fields, widget=forms.CheckboxSelectMultiple, required = False)
    dept_fields = [(str(field),str(field)) for field in Department.objects.all()]
    enquiry_type = forms.ChoiceField(choices=dept_fields, required=False, initial='Marketing')
    date_order = forms.ChoiceField(choices = (('Ascending','Ascending'),('Descending','Descending')), required=False)
    search = forms.CharField(max_length=50, required=False)