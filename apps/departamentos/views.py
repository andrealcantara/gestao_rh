from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Departamento

class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_logada)
        return queryset

class DepartamentosDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('listar_departamentos')

class DepartamentosUpdate(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentosCreate(CreateView):
    model = Departamento
    fields = ['nome']


    def form_valid(self, form):
        departamento = form.save(commit=False)
        empresa_logada = self.request.user.funcionario.empresa
        departamento.empresa = empresa_logada
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)