from .models import SpLic
from django.forms import ModelForm, TextInput, DateInput

class SpLicForm(ModelForm):
    class Meta:
        model = SpLic
        fields = ['id', 'fc_mo', 'name', 'c_prof', 'date_b','date_e']
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
                'placeholder': 'профиль'
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