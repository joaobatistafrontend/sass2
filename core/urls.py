
from django.contrib import admin
from django.urls import path,include
from .views import *
from .visivel import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('perfil/', PerfilVews.as_view(), name='perfil'),
    path('criar-prof/', CriarProfissionalView.as_view(), name='prof'),
    path('criar-servi/', CriarSevicosView.as_view(), name='servi'),
    path('criar-horario/', CriarHorarioViwe.as_view(), name='horario'),


    path('<slug:empresa_slug>/home/', HomeViews.as_view(),name='home'),
    path('<slug:empresa_slug>/prof/', ProfissionalView.as_view(), name='profissionais'),

    path('<slug:empresa_slug>/servicos/', ServicosViews.as_view(), name='servicos'),
    path('<slug:empresa_slug>/servico/<int:servico_id>/profissionais/', ProfissionaisPorServicoView.as_view(), name='profissionais_list'),
    path('<slug:empresa_slug>/horariosporprofissional/<int:profissional_id>/', HorariosPorProfissionalViews.as_view(), name='horariosoprofissionais'),
    #path('<slug:empresa_slug>/agendamentoprofissionais/<int:profissional_id>/', AgendamentoPorProfissionalView.as_view(), name='agendamentoprofissionais'),

    path('<slug:empresa_slug>/horarios/', HorarioAtendimentoViwe.as_view(), name='horariosempresa'),
    path('<slug:empresa_slug>/formhorarios/', AgendamentoView.as_view(), name='agendamento'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)