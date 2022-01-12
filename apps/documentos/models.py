from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos')
    pertence = models.ForeignKey(Funcionario, on_delete=models.deletion.PROTECT)

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('editar_funcionarios', args=[self.pertence.id])
