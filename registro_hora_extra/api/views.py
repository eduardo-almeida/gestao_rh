from rest_framework import viewsets
from rest_framework import permissions
from registro_hora_extra.api.serializers import RegistroHoraExtraSerializer
from registro_hora_extra.models import RegistroHoraExtra

class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    permission_classes = [permissions.IsAuthenticated]