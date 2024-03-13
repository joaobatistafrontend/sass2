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


class PerfilVews(View):
    def get(self,request):
        # Obtém o perfil do usuário logado
        profile = request.user  # Supondo que o perfil do usuário esteja associado ao modelo User
        #profile = request.user        

        # Obtém a empresa associada ao dono (perfil) do usuário logado
        #empresa = profile.dono.empresa  # Supondo que o dono tenha um relacionamento OneToOne com Empresa
        empresa = Empresa.objects.filter(dono=self.request.user).first()
        # Obtém os profissionais associados à empresa
        profissionais = Profissional.objects.filter(empresa=empresa)

        return render(request, 'perfil.html', {'profile': profile, 'empresa': empresa, 'profissionais': profissionais})

class CriarProfissionalView(LoginRequiredMixin, CreateView):
    model = Profissional
    fields = ['nome', 'especialidade']
    template_name = 'criar_profissional.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        empresa = Empresa.objects.filter(dono=self.request.user).first()
        if empresa:
            form.instance.empresa = empresa
            return super().form_valid(form)
        else:
            return HttpResponseForbidden("Você não tem permissão para criar profissionais nesta empresa.")

class CriarSevicosView(LoginRequiredMixin, CreateView):
    model = Servicos
    fields = ['servico']
    template_name = 'criar_servicos.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
            empresa = Empresa.objects.filter(dono=self.request.user).first()
            if empresa:
                form.instance.empresa = empresa
                return super().form_valid(form)
            else:
                return HttpResponseForbidden("Você não tem permissão para criar serviços nesta empresa.")

class CriarHorarioViwe(LoginRequiredMixin, CreateView):
    model = HorarioAtendimento
    fields = ['hora_abertura', 'duracao_minutos']
    template_name = 'criar_horarios.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
            empresa = Empresa.objects.filter(dono=self.request.user).first()
            if empresa:
                form.instance.empresa = empresa
                return super().form_valid(form)
            else:
                return HttpResponseForbidden("Você não tem permissão para criar horarios nesta empresa.")

        
'''    def form_valid(self, form):
        form.instance.empresa = self.request.user.empresa  # Defina a empresa com base no usuário logado
        return super().form_valid(form)
'''
    
