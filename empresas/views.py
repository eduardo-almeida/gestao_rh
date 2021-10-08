from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        colaborador = self.request.user.colaborador
        colaborador.empresa = obj
        colaborador.save()
        return HttpResponse('Ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']

