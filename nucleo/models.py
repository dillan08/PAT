from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # custom fields for user
    nivelEstudios = models.CharField(max_length=30)

class OAT(models.Model):
    nomOAT = models.CharField(max_length=45)
    descOAT = models.CharField(max_length=120)
    fechOAT = models.DateTimeField(auto_created=True, auto_now_add=True)
    textOAT = models.CharField(max_length=2000)

class Curso(models.Model):
    nomCurso = models.CharField(max_length=45)
    desCurso = models.CharField(max_length=120)
    etiqCurso = models.CharField(max_length=120)

class Grupo(models.Model):
    idGrupo = models.IntegerField()

class Actividad(models.Model):
    descActividad = models.CharField(max_length=45)
    fechActividad = models.DateTimeField(auto_now_add=True)
    textActividad = models.CharField(max_length=2000)
    nomActividad = models.CharField(max_length=45)

class Alumno(models.Model):
    idUsuario = PerfilUsuario.user
    idGrupo = Grupo.id
    idAlumno = models.IntegerField()

class Interes(models.Model):
    nombre = models.CharField(max_length=20)