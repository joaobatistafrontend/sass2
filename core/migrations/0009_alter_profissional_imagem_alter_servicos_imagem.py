# Generated by Django 4.2.11 on 2024-03-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_servicos_imagem_alter_profissional_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
