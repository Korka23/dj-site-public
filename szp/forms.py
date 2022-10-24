from .models import SzpLic
from django import forms
from app.models import FC_MO_CHOICES, IDPR_CHOICES
from sp.models import C_PROF_CHOICES

class SzpLicForm(forms.ModelForm):
    class Meta:
        model = SzpLic
        fc_mo = forms.ChoiceField(choices=FC_MO_CHOICES)
        c_prof = forms.ChoiceField(choices=C_PROF_CHOICES)
        idpr = forms.ChoiceField(choices=IDPR_CHOICES)
        fields = ['id', 'fc_mo', 'name','date_b','date_e']
        widgets = {
            "id_prof": forms.TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'id проф'
            }),

            "name": forms.TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название МО'
            }),
            "date_b": forms.DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),

            "date_e": forms.DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            }),
        }

class SzpLicForm2(forms.ModelForm):
    class Meta:
        model = SzpLic
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
            "lic_num": forms.TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Приказ'
            }),
            "deleted": forms.CheckboxInput(attrs={
                'class': 'from-control',
                'placeholder': 'Вы уверены?'
            })
        }