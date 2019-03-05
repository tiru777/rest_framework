from . models import Employee
from django.forms import forms

class EmployeeForms(forms.Form):
    model = Employee
    fields = '__all__'
