from .models import SpLic
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput

class SpLicForm(ModelForm):
    class Meta:
        model = SpLic
        fields = ['id', 'fc_mo', 'name', 'c_prof','idpr', 'date_b','date_e','deleted']
        widgets = {
            "id": TextInput(attrs={
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
                'placeholder': 'код профиля'
            }),
            "idpr": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Федеральный код'
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