import io

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from .models import Colaborador
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


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
    success_url = reverse_lazy('list_colaboradores')

class ColaboradoresCreate(CreateView):
    model = Colaborador
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        colaborador = form.save(commit=False)
        colaborador.empresa = self.request.user.colaborador.empresa
        username = colaborador.nome.split(' ')[0] + colaborador.nome.split(' ')[1]
        colaborador.user = User.objects.create(username=username)
        colaborador.save()
        return super(ColaboradoresCreate, self).form_valid(form)

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not  pdf.err:
            response = HttpResponse(response.getvalue(),
                                    content_type='application/pdf')
            response['content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):
    def get(self, request):
        params = {
            'today': 'Variavel Today',
            'sales': 'Variavel Sale',
            'request': request
        }
        return Render.render('colaboradores/relatorio.html', params, 'myfile')