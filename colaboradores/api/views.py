from rest_framework import viewsets
from rest_framework import permissions
from colaboradores.api.serializers import ColaboradorSerializer
from colaboradores.models import Colaborador
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    #permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
