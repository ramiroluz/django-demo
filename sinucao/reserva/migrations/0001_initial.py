# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('data_registro', models.DateTimeField(verbose_name='data de registro')),
                ('endereco', models.CharField(max_length=200)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
                ('celular', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preco_hora', models.IntegerField(default=20)),
                ('titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_reserva', models.DateTimeField(verbose_name='data de registro da reserva')),
                ('data_jogo', models.DateTimeField(verbose_name='data de uso da mesa')),
                ('cliente', models.ForeignKey(to='reserva.Cliente')),
                ('mesa', models.ForeignKey(to='reserva.Mesa')),
            ],
        ),
    ]
