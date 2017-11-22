# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id_disciplina', models.AutoField(primary_key=True, serialize=False)),
                ('carga_horaria', models.IntegerField()),
                ('teoria', models.DecimalField(decimal_places=3, max_digits=3)),
                ('pratica', models.DecimalField(decimal_places=3, max_digits=3)),
                ('ementa', models.TextField()),
                ('competencias', models.TextField()),
                ('habilidades', models.TextField()),
                ('conteudo', models.TextField()),
                ('bibliografia_basica', models.TextField()),
                ('bibliografica_complementar', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
