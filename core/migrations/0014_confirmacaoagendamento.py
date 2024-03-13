# Generated by Django 4.2.11 on 2024-03-13 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_horarioatendimento_servicos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmacaoAgendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(blank=True, max_length=100, null=True)),
                ('celular_usuario', models.CharField(blank=True, max_length=20, null=True)),
                ('data_aniversario_usuario', models.DateField(blank=True, null=True)),
                ('horario_atendimento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.horarioatendimento')),
            ],
        ),
    ]
