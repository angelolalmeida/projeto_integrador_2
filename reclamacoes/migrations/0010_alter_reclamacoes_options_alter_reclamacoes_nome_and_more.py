# Generated by Django 4.2.6 on 2023-10-27 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamacoes', '0009_alter_reclamacoes_acompanhar_reclamacao_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reclamacoes',
            options={'verbose_name': '', 'verbose_name_plural': ''},
        ),
        migrations.AlterField(
            model_name='reclamacoes',
            name='nome',
            field=models.CharField(max_length=100, null=True, verbose_name='NOME COMPLETO'),
        ),
        migrations.AlterModelTable(
            name='reclamacoes',
            table='',
        ),
    ]
