# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-20 17:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(default=0)),
                ('tipo', models.CharField(choices=[('JU', 'JUEGO'), ('EX', 'EXAMEN')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCurso', models.CharField(max_length=45)),
                ('desCurso', models.CharField(max_length=120)),
                ('etiqCurso', models.CharField(max_length=120)),
                ('maxAlumnos', models.IntegerField(default=0)),
                ('grupo', models.CharField(max_length=15)),
                ('escuela', models.CharField(max_length=20)),
                ('esEscolar', models.BooleanField(default=False)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('cursos', models.ManyToManyField(related_name='Curso_Has_Inter', to='nucleo.Curso')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('video', models.CharField(max_length=255)),
                ('metadata', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomOAT', models.CharField(max_length=45)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.CharField(max_length=2000)),
                ('archivos', models.CharField(max_length=120)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivelEstudios', models.CharField(choices=[('SN', 'Sin Estudios'), ('PR', 'Primaria'), ('SE', 'Secundaria'), ('MS', 'Media Superior'), ('SU', 'Superior'), ('MA', 'Maestria'), ('DO', 'Doctorado')], default='SN', max_length=2)),
                ('descripcion', models.CharField(max_length=120)),
                ('imagen', models.ImageField(upload_to='')),
                ('esAlumno', models.BooleanField(default=False, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PerfilUsuario',
            },
        ),
        migrations.AddField(
            model_name='multimedia',
            name='oast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.OAT'),
        ),
        migrations.AddField(
            model_name='curso',
            name='oats',
            field=models.ManyToManyField(related_name='Curso_has_OAT', to='nucleo.OAT'),
        ),
        migrations.AddField(
            model_name='curso',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='usuarios',
            field=models.ManyToManyField(related_name='Curso_has_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleo.Curso'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actividad',
            name='cursos',
            field=models.ManyToManyField(related_name='Cur_has_Act', to='nucleo.Curso'),
        ),
    ]
