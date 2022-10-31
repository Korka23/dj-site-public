import django_filters
from .models import LicAppNew, C_SERV_CHOICES, FC_MO_CHOICES_FILT, IDPR_CHOICES, FC_NAME_CHOICES_2, CLEAR_C_SERV

class SnippetFilter(django_filters.FilterSet):

    fc_mo=django_filters.ChoiceFilter(label='КОД МО', choices=FC_MO_CHOICES_FILT)
    name = django_filters.ChoiceFilter(label='Название МО', choices=FC_NAME_CHOICES_2)
    c_serv_cod =django_filters.ChoiceFilter(label='КОД СПЕЦИАЛЬНОСТИ НАШ', choices=C_SERV_CHOICES)
    c_serv = django_filters.ChoiceFilter(label='КОД СПЕЦИАЛЬНОСТИ C_SERV', choices=CLEAR_C_SERV)
    idpr_cod =django_filters.ChoiceFilter(label='ФЕДЕРАЛЬНЫЙ КОД', choices=IDPR_CHOICES)
    idpr= django_filters.ChoiceFilter(label='ФЕДЕРАЛЬНЫЙ КОД IDPR',choices=CLEAR_C_SERV )
    class Meta:
        model = LicAppNew
        fields=('fc_mo','name','c_serv_cod','c_serv', 'idpr_cod','idpr')