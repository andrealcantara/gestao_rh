from django.forms import ModelForm

from .models import RegistroHoraExtra
from ..funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):

    def __init__(self, user, create=False, *args, **kwargs):
        self.create = create
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=user.funcionario.empresa)

        # if not create:
        #     del self.fields['funcionario']

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'hora_extra']
