from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    module = RegistroHoraExtra

    def get_queryset(self):
        return RegistroHoraExtra.objects.filter(funcionario__empresa=self.request.user.funcionario.empresa)



class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'hora_extra']


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('listar_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'hora_extra']

