from .models import LicAppNew
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput

class LicAppNewForm(ModelForm):
    class Meta:
        model = LicAppNew
        fields = ['id_prof', 'fc_mo', 'name', 'date_b', 'idpr','disp', 'date_e', 'lic_num', 'c_serv', 'deleted']
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
            "date_b": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),
            "idpr": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Федеральный профиль'
            }),
            "disp": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Диспан'
            }),#Под вырез мб
            "date_e": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            }),
            "lic_num": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Приказ'
            }),
            "c_serv": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Профиль кода специальности'
            }),
            "deleted": TextInput (attrs={
                'class': 'from-control',
                'placeholder': 'Вы уверены?'
            })

        }