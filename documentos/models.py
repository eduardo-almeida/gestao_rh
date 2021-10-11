from django.db import models
from django.urls import reverse

from colaboradores.models import Colaborador


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_colaboradores', args=[self.colaborador.id])
        #return reverse('colaboradores/')

    def __str__(self):
        return self.descricao
