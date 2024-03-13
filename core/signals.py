'''from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Empresa

@receiver(post_save, sender=User)
def associar_empresa_ao_usuario(sender, instance, created, **kwargs):
    if created:
        # Criar ou recuperar a empresa associada ao usuário
        empresa = Empresa.objects.create(dono=instance, nome=f'{instance.username}')

        # Associar a empresa ao usuário
        instance.empresa = empresa
        instance.save()
'''
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Empresa, Profissional

@receiver(post_save, sender=User)
def associar_empresa_ao_usuario(sender, instance, created, **kwargs):
    if created:
        # Criar ou recuperar a empresa associada ao usuário
        empresa = Empresa.objects.create(dono=instance, nome=f'{instance.username}')

        # Criar um profissional associado à empresa do usuário
        #Profissional.objects.create(empresa=empresa, nome='Nome do Profissional', especialidade='Especialidade do Profissional')

        # Associar a empresa ao usuário
        instance.empresa = empresa
        instance.save()

