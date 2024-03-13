
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
    path('prof/', CriarProfissionalView.as_view(), name='prof'),
    path('servi/', CriarSevicosView.as_view(), name='servi'),
    path('horario/', CriarHorarioViwe.as_view(), name='horario'),


    path('<slug:empresa_slug>/home/', HomeViews.as_view(),name='home'),
    path('<slug:empresa_slug>/prof/', ProfissionalView.as_view(), name='profissionais'),
    path('<slug:empresa_slug>/servicos/', ServicosViews.as_view(), name='servicos'),

    path('<slug:empresa_slug>/servico/<int:servico_id>/profissionais/', ProfissionaisPorServicoView.as_view(), name='profissionais_list'),
    path('<slug:empresa_slug>/horarios/', HorarioAtendimentoViwe.as_view(), name='horariosempresa'),
    path('<slug:empresa_slug>/formhorarios/', AgendamentoView.as_view(), name='agendamento'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)