import django_filters
from .models import SpLic, IDPR_CHOICES, FC_NAME_CHOICES_2, C_PROF_CHOICES, CLEAR_C_PROF
from app.models import  FC_MO_CHOICES_FILT, CLEAR_IDPR

class SnippetFilter(django_filters.FilterSet):

    fc_mo=django_filters.ChoiceFilter(label='КОД МО', choices=FC_MO_CHOICES_FILT)
    name = django_filters.ChoiceFilter(label='Название МО', choices=FC_NAME_CHOICES_2)
    c_prof =django_filters.ChoiceFilter(label='КОД ПРОФИЛЯ НАШ', choices=C_PROF_CHOICES)
    idpr=django_filters.ChoiceFilter(label='НАЗВАНИЕ ФЕДЕРАЛЬНОГО КОДА', choices=IDPR_CHOICES)
    c_prof_cod=django_filters.ChoiceFilter(label='ПРОФИЛЬ НАШ C_PROF', choices=CLEAR_C_PROF)
    idpr_cod=django_filters.ChoiceFilter(label='КОД ФЕДЕРАЛЬНЫЙ', choices=CLEAR_IDPR)
    class Meta:
        model = SpLic
        fields=('fc_mo','name','c_prof_cod','c_prof','idpr_cod','idpr')