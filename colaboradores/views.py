from .models import Colaborador
from django.views.generic import ListView, UpdateView, DeleteView


class ColaboradoresList(ListView):
    model = Colaborador

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa=empresa_logada)

class ColaboradoresEdit(UpdateView):
    model = Colaborador
    fields = ['nome', 'departamentos']

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa=empresa_logada)

class ColaboradoresDelete(DeleteView):
    model = Colaborador
    success_url = 'list_colaboradores'

