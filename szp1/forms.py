from .models import Szp1Lic
from django.forms import ModelForm, TextInput, DateInput

class Szp1LicForm(ModelForm):
    class Meta:
        model = Szp1Lic
        fields = ['id', 'fc_mo', 'name','c_prof','idpr', 'date_b','date_e']
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
                'placeholder': 'Код профиля (Наш)'
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
        }