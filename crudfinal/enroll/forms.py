from django import forms
from . models import Employee

class EmployeeDetail(forms.ModelForm):
    class Meta:
        
        model = Employee

        fields = ['name','department','city','salary']

        widgets = {'name':forms.TextInput({'placeholder':'Enter your name here'})}

        