# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alunos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alunos',
            options={'verbose_name': 'Aluno', 'verbose_name_plural': 'Alunos'},
        ),
        migrations.RemoveField(
            model_name='alunos',
            name='id',
        ),
        migrations.AlterField(
            model_name='alunos',
            name='celular',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='ra',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]