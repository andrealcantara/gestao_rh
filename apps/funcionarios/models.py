from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.deletion.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.deletion.PROTECT,
                                null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('listar_funcionarios')

    @property
    def total_horas_extras(self):
        return self.registrohoraextra_set \
                        .filter(utilizada=False) \
                        .aggregate(Sum('hora_extra'))['hora_extra__sum'] or 0
