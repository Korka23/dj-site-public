from .models import *
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput, Select, RadioSelect
from django import forms


class LicAppNewForm(ModelForm):

    class Meta:
        model = LicAppNew
        fc_mo = forms.ChoiceField(choices=C_SERV_CHOICES)
        c_serv = forms.ChoiceField(choices=C_SERV_CHOICES)
        idpr = forms.ChoiceField(choices=IDPR_CHOICES)
        fields = ['id_prof', 'fc_mo', 'name', 'date_b', 'disp', 'date_e', 'lic_num', 'deleted','c_serv']
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
            }),
            #"c_serv":forms.ChoiceField(attrs={'style':'width:200px'})
        }

class LicAppNewForm2(ModelForm):

    class Meta:
        model = LicAppNew
        fields = ['id_prof', 'fc_mo', 'name', 'date_b', 'disp', 'date_e', 'lic_num', 'deleted','idpr','c_serv']
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

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = LicAppNew
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['fc_mo'].queryset = City.objects.none()
        self.fields['fc_mo'].queryset = LicAppNew.objects.none()
#
'''
        if 'fc_mo' in self.data:
            try:
                #fc_mo = int(self.data.get('fc_mo'))
                fc_mo = int(self.data.get('fc_mo'))
                self.fields['fc_mo'].queryset = LicAppNew.objects.filter(fc_mo=fc_mo).order_by('fc_mo')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['fc_mo'].queryset = self.instance.LicAppNew.objects.order_by('fc_mo')
'''
#
'''
        widjets ={
            "fc_mo": RadioSelect( LicAppNew.fc_mo == fc_mo_choices),
            "name": Select(),
            "date_b": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата начала действия лицензии'
            }),
            "idpr": Select(),
            "disp": Select(),#Под вырез мб
            "date_e": DateInput(attrs={
                'class': 'from-control',
                'placeholder': 'Дата конца действия лицензии'
            }),
            "lic_num": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Приказ'
            }),
            "c_serv": Select(),
            "deleted": CheckboxInput(attrs={
                'class': 'from-control',
                'placeholder': 'Вы уверены?'
            })
        }
'''
#asd
'''
        def __init__(self, *args, **kwargs):
            self.fields['fc_mo'].widget.attrs.update({"class": "form-control"})
            # or iterate over field to add class for each field
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': "form-control"})
        '''
class djFormAp(ModelForm):
    class Meta:
        model = LicAppNew
        fields = ['fc_mo']