from django.db import models
from colaboradores.models import Colaborador


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao