# Generated by Django 4.2.11 on 2024-03-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_horarioatendimento_confirmacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarioatendimento',
            name='confirmacao',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
