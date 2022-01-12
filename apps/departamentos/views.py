from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Departamento

class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_logada)
        return queryset

class DepartamentosCreate(CreateView):
    model = Departamento
    fields = ['nome']


    def form_valid(self, form):
        departamento = form.save(commit=False)
        empresa_logada = self.request.user.funcionario.empresa
        departamento.empresa = empresa_logada
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)