from rest_framework import serializers
from colaboradores.models import Colaborador
from registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class ColaboradorSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Colaborador
        fields = ['nome', 'user', 'departamentos', 'total_horas_extras', 'registrohoraextra_set']
