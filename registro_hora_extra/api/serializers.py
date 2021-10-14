from rest_framework import serializers
from registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'colaborador', 'horas', 'utilizada']
