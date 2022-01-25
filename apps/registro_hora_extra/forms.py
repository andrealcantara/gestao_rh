from django.forms import ModelForm

from .models import RegistroHoraExtra
from ..funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):

    def __init__(self, empresa, funcionario_id=False, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=empresa)

        if funcionario_id:
            self.fields['funcionario'].initial = funcionario_id
            # del self.fields['funcionario']
            # self.fields['funcionario'].widget.attrs['disabled'] = 'disabled'
            # self.fields['funcionario'].editable = False
            # self.fields['funcionario'].empty_label = None
            # self.fields['funcionario'].required = False

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'hora_extra']
        use_required_attribute = False
