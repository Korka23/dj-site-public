from .models import dj_ksg_p
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput

class KSGForms(ModelForm):
    class Meta:
        model=dj_ksg_p
        fields=['name','c_prof','smj_prof','KSG','deleted','date_e','date_b']
        widgets={
            "name": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название КСГ'
            }),
            "c_prof": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Профиль'
            }),
            "smj_prof": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Смежный профиль',#this should be array
            }),
            "KSG": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'КСГ'
            }),
            "deleted": CheckboxInput(attrs={
                'class': 'from-control',
                'placeholder': 'Вы уверены?'
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


