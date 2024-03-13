from django import forms
from .models import ConfirmacaoAgendamento

class ConfirmacaoAgendamentoForm(forms.ModelForm):
    class Meta:
        model = ConfirmacaoAgendamento
        fields = ['horario_atendimento', 'nome_usuario', 'celular_usuario', 'data_aniversario_usuario']