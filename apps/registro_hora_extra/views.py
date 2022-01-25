import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra


def get_form_kwargs_modal(clazz, self):
    kwargs = super(clazz, self).get_form_kwargs()
    kwargs.update({'empresa': self.request.user.funcionario.empresa, 'funcionario_id': self.kwargs['funcionario_id']})
    return kwargs


def reverse_default(self, url_name='editar_funcionarios'):
    return reverse_lazy(url_name, kwargs={'pk': self.kwargs['funcionario_id']})





class HoraExtraList(ListView):
    module = RegistroHoraExtra

    def get_queryset(self):
        return RegistroHoraExtra.objects. \
            filter(funcionario__empresa=self.request.user.funcionario.empresa)


class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('listar_hora_extra')

    def get_form_kwargs(self):
        return get_form_kwargs_modal(HoraExtraUpdate, self)


class HoraExtraByFuncionarioUpdate(HoraExtraUpdate):
    def get_success_url(self):
        return reverse_default(self)


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('listar_hora_extra')


class HoraExtraUtilizadaToggle(View):
    def post(self, *args, **kwargs):
        hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        hora_extra.utilizada = not hora_extra.utilizada
        hora_extra.save()
        response = {'status': 'update',
                    'mensagem': 'Requesição Executada com sucesso',
                    'value': hora_extra.utilizada}
        return HttpResponse(json.dumps(response),
                            content_type='application/json')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('listar_hora_extra')

    def get_form_kwargs(self):
        return get_form_kwargs_modal(HoraExtraCreate, self)


class HoraExtraByFuncionarioCreate(HoraExtraCreate):
    def get_success_url(self):
        return reverse_default(self)
