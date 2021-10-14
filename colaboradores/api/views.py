from rest_framework import viewsets
from rest_framework import permissions
from colaboradores.api.serializers import ColaboradorSerializer
from colaboradores.models import Colaborador

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    permission_classes = [permissions.IsAuthenticated]