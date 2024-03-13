from django.shortcuts import render,redirect,HttpResponse
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView,CreateView,View,ListView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .form import *
from django.views.generic.edit import FormView

class HomeViews(View):
    def get(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissionais = Profissional.objects.filter(empresa=empresa)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa)

        return render(request, 'visivel/index.html',{'empresa':empresa})

class ProfissionalView(View):
    def get(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissionais = Profissional.objects.filter(empresa=empresa)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa)

        return render(request, 'visivel/testprof.html',{'empresa':empresa, 'profissionais' : profissionais})


class ServicosViews(View):
    def get(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissionais = Profissional.objects.filter(empresa=empresa)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa)
        servicos = Servicos.objects.filter(empresa=empresa)
        return render(request, 'visivel/servicos.html',{'empresa':empresa, 'servicos' : servicos})
    
class ProfissionaisPorServicoView(View):
    def get(self, request, empresa_slug, servico_id):
        profissionais = Profissional.objects.filter(empresa__slug=empresa_slug, especialidade__id=servico_id)
        return render(request, 'visivel/profissionais_por_servico.html', {'profissionais': profissionais})
    

class HorarioAtendimentoViwe(View):
    def get(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissionais = Profissional.objects.filter(empresa=empresa)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa, confirmacao=False)

        return render(request, 'visivel/horarios.html',{'empresa':empresa, 'profissionais' : profissionais, 'horarios' : horarios})
    
class AgendamentoView(View):
    def get(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissionais = Profissional.objects.filter(empresa=empresa)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa, confirmacao=False)
        form = ConfirmacaoAgendamentoForm()  # Adiciona um formulário de confirmação de agendamento

        return render(request, 'visivel/formconfim.html', {'empresa': empresa, 'profissionais': profissionais, 'horarios': horarios, 'form': form})

    def post(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa,confirmacao=False)
        profissionais = Profissional.objects.filter(empresa=empresa)

        form = ConfirmacaoAgendamentoForm(request.POST)
        if form.is_valid():
            # Salva o formulário se for válido
            confirmacao = form.save(commit=False)  # Salva o objeto, mas não persiste no banco de dados ainda
            confirmacao.horario_atendimento.confirmacao = True  # Atualiza o campo confirmacao do HorarioAtendimento
            confirmacao.horario_atendimento.save()  # Salva a alteração no banco de dados
            form.save()  # Salva a confirmação do agendamento

            return render(request, 'visivel/horarios.html', {'empresa': empresa, 'profissionais': profissionais, 'horarios': horarios, 'form': form})
        else:
            # Se o formulário não for válido, reexibe a página com os erros
            return render(request, 'visivel/horarios.html', {'empresa': empresa, 'profissionais': profissionais, 'horarios': horarios, 'form': form})