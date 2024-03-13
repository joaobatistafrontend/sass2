from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image

class Empresa(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

        
@receiver(pre_save, sender=Empresa)
def atualizar_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.nome)

        # Verificar se o slug gerado já existe
        if Empresa.objects.filter(slug=instance.slug).exists():
            # Se o slug já existe, adicionar um número para torná-lo único
            count = 1
            while Empresa.objects.filter(slug=instance.slug).exists():
                instance.slug = f"{slugify(instance.nome)}-{count}"
                count += 1
class Servicos(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
    servico = models.CharField(max_length=100, null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens/',blank=True, null=True)

    def __str__(self):
        return f'{self.servico}'

class Profissional(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/',blank=True, null=True)
    especialidade = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} - {self.especialidade}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            img = Image.open(self.imagem.path)

            # Defina as larguras e alturas desejadas
            largura_padrao = 168
            altura_padrao = 168

            # Redimensione a imagem
            img.thumbnail((largura_padrao, altura_padrao))
            img.save(self.imagem.path)

class HorarioAtendimento(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE,null=True, blank=True)
    hora_abertura = models.TimeField()
    duracao_minutos = models.IntegerField()
    def __str__(self):
        return f'{self.hora_abertura} - {self.duracao_minutos} minutos'