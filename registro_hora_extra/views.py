import csv
import json

import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .form import RegistroHoraExtraForm
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return RegistroHoraExtra.objects.filter(colaborador__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    #success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        colaborador = self.request.user.colaborador
        response = json.dumps({'mensagem': 'Requisicao executada', 'horas': float(colaborador.total_horas_extras)})

        return HttpResponse(response, content_type='application/json')

class ExportarParaCSV(View):
    def get(self, request):
        filename = 'arquivo'
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition'] = 'attachment; filename=%s.csv' % filename

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionario', 'Horas'])
        for registro in registro_he:
            writer.writerow([registro.id, registro.motivo, registro.colaborador, registro.horas])
        return response

class ExportarParaExcel(View):
    def get(self, request):
        filename = 'arquivoExcel'
        response = HttpResponse(content_type='application/ms-excel')
        response['content-Disposition'] = 'attachment; filename=%s.csv' % filename

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_number = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Colaborador', 'Horas']

        for column_num in range(len(columns)):
            ws.write(row_number, column_num, columns[column_num], font_style)

        font_style = xlwt.XFStyle()
        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        row_number = 1

        for registro in registros:
            ws.write(row_number, 0, registro.id)
            ws.write(row_number, 1, registro.motivo)
            ws.write(row_number, 2, registro.colaborador.nome)
            ws.write(row_number, 3, registro.horas)
            row_number+=1

        wb.save(response)
        return response

