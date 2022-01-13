from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DeleteView

from apps.documentos.models import Documento
from apps.funcionarios.models import Funcionario


class DocumentosList(ListView):
    model = Documento
    def get_queryset(self):
        return Documento.objects.filter(pertence=Funcionario.objects.filter(id=self.request.get['pk']))

class DocumentosDelete(DeleteView):
    model = Documento


class DocumentosCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        id_funcionario = self.kwargs['id_funcionario']
        form.instance.pertence_id = id_funcionario
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

