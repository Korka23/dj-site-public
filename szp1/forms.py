from .models import Szp1Lic
from django.forms import ModelForm, TextInput, DateInput
from django import forms
from app.models import *
from sp.models import C_PROF_CHOICES

class Szp1LicForm(ModelForm):
    class Meta:
        model = Szp1Lic
        fc_mo = forms.ChoiceField(choices=FC_MO_CHOICES)
        c_prof = forms.ChoiceField(choices=C_PROF_CHOICES)
        idpr = forms.ChoiceField(choices=IDPR_CHOICES)
        fields = ['id', 'date_b','date_e']
        widgets = {
            "id": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'id проф'
            }),
            "date_b": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),

            "date_e": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            }),
        }
class Szp1LicForm2(forms.ModelForm):
    class Meta:
        model = Szp1Lic
        fields = ['id', 'fc_mo', 'name', 'date_b',  'date_e',  'deleted', 'idpr', 'c_prof']
        widgets = {
            "date_b": forms.DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),
            "disp": forms.TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Диспан'
            }),
            "date_e": forms.DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            }),
            "deleted": forms.CheckboxInput(attrs={
                'class': 'from-control',
                'placeholder': 'Вы уверены?'
            })
        }