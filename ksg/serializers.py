from django.conf import settings
from rest_framework import serializers

from ksg.models import dj_ksg_p


class MusicSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    last_modify_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    created = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = dj_ksg_p
        # fields = '__all__'
        fields = ('id', 'name', 'c_prof', 'smj_prof', 'ksg')