from django.db import models
from apps.colaboradores.models import Colaborador
from django.shortcuts import reverse


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('edit_colaborador', args=[self.colaborador_id])

    def __str__(self):
        return self.descricao
