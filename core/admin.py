from django.contrib import admin
from .models import *

admin.site.register(Empresa)
admin.site.register(Servicos)
admin.site.register(Profissional)
admin.site.register(HorarioAtendimento)

