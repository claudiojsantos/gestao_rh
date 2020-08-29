from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.nome
