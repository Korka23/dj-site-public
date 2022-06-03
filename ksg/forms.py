from .models import dj_ksg_p,LicDop, LicMash
from django.forms import ModelForm, TextInput, DateInput

class KSGForms(ModelForm):
    class Meta:
        model=dj_ksg_p
        fields=['name','c_prof','smj_prof','KSG']
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
            })
        }


class LicDopForm(ModelForm):
    class Meta:
        model = LicDop
        fields = ['id_prof', 'id_mo', 'c_prof']
        widgets = {
            "id_prof": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Номер МО'
            }),
            "id_mo": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название МО'
            }),
            "c_prof": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Профиль'
            })
        }

class LicMashForm(ModelForm):
    class Meta:
        model = LicMash
        fields = ['id_prof', 'fc_mo', 'name', 'c_prof', 'date_b', 'date_e']
        widgets = {
            "id_prof": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'id проф'
            }),
            "fc_mo": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Номер МО'
            }),
            "name": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название МО'
            }),
            "c_prof": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Профиль'
            }),
            "date_b": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),
            "date_e": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            })
        }
