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
        servicos = Servicos.objects.filter(empresa=empresa)
        profissionais = Profissional.objects.filter(empresa=empresa)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa)

        return render(request, 'visivel/index.html',{'empresa':empresa,  'servicos' : servicos, 'profissionais' : profissionais})

class ProfissionalView(View):
    def get(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissionais = Profissional.objects.filter(empresa=empresa)
        horarios = HorarioAtendimento.objects.filter(empresa=empresa)

        return render(request, 'visivel/testprof.html',{'empresa':empresa, 'profissionais' : profissionais})


class ServicosViews(View):
    def get(self, request, empresa_slug):
        empresa = Empresa.objects.get(slug=empresa_slug)
        servicos = Servicos.objects.filter(empresa=empresa)
        return render(request, 'visivel/servicos.html',{'empresa':empresa, 'servicos' : servicos})
    
class ProfissionaisPorServicoView(View):
    def get(self, request, empresa_slug, servico_id):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissionais = Profissional.objects.filter(empresa__slug=empresa_slug, especialidade__id=servico_id)
        return render(request, 'visivel/profissionais_por_servico.html', {'empresa':empresa, 'profissionais': profissionais})
    

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
        
        # Filtra apenas os horários livres no formulário
        form = ConfirmacaoAgendamentoForm(horarios=horarios)

        return render(request, 'visivel/formconfim.html', {'empresa': empresa, 'profissionais': profissionais, 'form': form})

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
        



class HorariosPorProfissionalViews(View):
    def get(self, request, empresa_slug, profissional_id):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissional = Profissional.objects.get(id=profissional_id)
        horarios_livres = HorarioAtendimento.objects.filter(profissional=profissional,confirmacao=False)
        form = AgendamentoForm(horarios=horarios_livres)

        return render(request, 'visivel/agendamento_por_profissional.html', {'profissional': profissional, 'form':form,'horarios_livres':horarios_livres, 'empresa': empresa})    


''' 
class AgendamentoPorProfissionalView(View):
    def get(self, request, empresa_slug, profissional_id):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissional = Profissional.objects.get(id=profissional_id)
        horarios_livres = HorarioAtendimento.objects.filter(profissional=profissional, confirmacao=False)
        form = AgendamentoForm()

        return render(request, 'visivel/agendamento_por_profissional.html', {'profissional': profissional, 'form': form, 'empresa': empresa})

  def post(self, request, empresa_slug, profissional_id):
        empresa = Empresa.objects.get(slug=empresa_slug)
        profissional = Profissional.objects.get(id=profissional_id)
        horarios_livres = HorarioAtendimento.objects.filter(profissional=profissional, confirmacao=False)
        form = AgendamentoForm(request.POST)

        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.profissional = profissional
            agendamento.save()

            horario_selecionado = form.cleaned_data['horario_selecionado']
            horario_selecionado.confirmacao = True
            horario_selecionado.save()

            return redirect('sucesso_agendamento')

        return render(request, 'visivel/agendamento_por_profissional.html', {'profissional': profissional, 'horarios_livres': horarios_livres, 'form': form, 'empresa': empresa})'''