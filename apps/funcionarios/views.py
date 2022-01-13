import itertools

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']


class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('listar_funcionarios')


class FuncionariosCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        nome_funcionario = ''.join(nome.capitalize() for nome in itertools.islice(funcionario.nome.split(' '), 0, 2))
        funcionario.user = User.objects.create(username=nome_funcionario)
        funcionario.save()
        return super(FuncionariosCreate, self).form_valid(form)

