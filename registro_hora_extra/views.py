from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return RegistroHoraExtra.objects.filter(colaborador__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'colaborador', 'horas']


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'colaborador', 'horas']
