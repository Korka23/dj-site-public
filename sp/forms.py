from .models import SpLic
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput
from django import forms
from app.models import *
from .models import C_PROF_CHOICES

class SpLicForm(ModelForm):
    class Meta:
        model = SpLic
        fc_mo = forms.ChoiceField(choices=FC_MO_CHOICES)
        c_prof = forms.ChoiceField(choices=C_PROF_CHOICES)
        idpr = forms.ChoiceField(choices=IDPR_CHOICES)
        fields = ['id', 'name', 'date_b','date_e','deleted']
        widgets = {
            "id": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'id проф'
            }),
            "name": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название МО'
            }),
            "date_b": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),
            "date_e": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            }),
            "deleted": CheckboxInput(attrs={
                'class': 'from-control',
                'placeholder': 'Вы уверены?'
            })
        }


class SpLicForm2(ModelForm):
    class Meta:
        model = SpLic
        fields = ['id', 'fc_mo', 'name', 'date_b',  'date_e',  'deleted', 'idpr', 'c_prof']
        widgets = {
            "date_b": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),
            "disp": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Диспан'
            }),
            "date_e": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            }),
            "lic_num": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Приказ'
            }),
            "deleted": CheckboxInput(attrs={
                'class': 'from-control',
                'placeholder': 'Вы уверены?'
            })
        }
