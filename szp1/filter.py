import django_filters
from sp.models import C_PROF_CHOICES
from app.models import  FC_MO_CHOICES_FILT, IDPR_CHOICES, FC_NAME_CHOICES_2
from szp1.models import Szp1Lic

class SnippetFilter(django_filters.FilterSet):

    fc_mo=django_filters.ChoiceFilter(label='КОД МО', choices=FC_MO_CHOICES_FILT)
    name = django_filters.ChoiceFilter(label='Название МО', choices=FC_NAME_CHOICES_2)
    c_prof =django_filters.ChoiceFilter(label='КОД СПЕЦИАЛЬНОСТИ НАШ', choices=C_PROF_CHOICES)
    idpr=django_filters.ChoiceFilter(label='ФЕДЕРАЛЬНЫЙ КОД', choices=IDPR_CHOICES)

    class Meta:
        model = Szp1Lic
        fields=('fc_mo','name','c_prof','idpr')