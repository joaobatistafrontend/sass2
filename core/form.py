from django import forms
from .models import ConfirmacaoAgendamento

class ConfirmacaoAgendamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        horarios = kwargs.pop('horarios', None)  # Captura os horários passados como argumento
        super().__init__(*args, **kwargs)

        # Filtra as opções do campo de horário de atendimento
        if horarios is not None:
            self.fields['horario_atendimento'].queryset = horarios

    class Meta:
        model = ConfirmacaoAgendamento
        fields = ['horario_atendimento', 'nome_usuario', 'celular_usuario', 'data_aniversario_usuario']        

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = ConfirmacaoAgendamento
        fields = ['horario_atendimento', 'nome_usuario', 'celular_usuario', 'data_aniversario_usuario']

    def __init__(self, *args, **kwargs):
        horarios = kwargs.pop('horarios', None)  # Recebe os horários livres como um parâmetro extra
        super().__init__(*args, **kwargs)
        
        # Personalize o campo 'horario_atendimento' para mostrar apenas horários livres passados como contexto
        if horarios:
            self.fields['horario_atendimento'].queryset = horarios