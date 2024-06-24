from django import forms
from django.forms import ModelForm
from Oper.models import brillentsec,feedcalcusers


class Oper_forms(forms.ModelForm):
    class Meta:
        model=brillentsec
        fields='__all__'
       
class Oper1_forms(forms.ModelForm):
    class Meta:
        model=feedcalcusers
        fields='__all__'
