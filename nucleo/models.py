from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    # custom fields for user
    DEFAULT ='SN'
    NIVEL_CHOICES=(
        ('SN', 'Sin Estudios'),
        ('PR', 'Primaria'),
        ('SE', 'Secundaria'),
        ('MS', 'Media Superior'),
        ('SU', 'Superior'),
        ('MA', 'Maestria'),
        ('DO', 'Doctorado'),
    )
    nivelEstudios = models.CharField(max_length=2,
                                     choices=NIVEL_CHOICES,
                                     default=DEFAULT
                                     )
    descripcion = models.CharField(max_length=120)
    imagen = models.ImageField(max_length=None)#, allow_empty_file=True)
    esAlumno=models.BooleanField(editable=False, default=False)
    def __str__(self):
        return self.nivelEstudios + ' ' + self.descripcion

    class Meta:
        db_table = 'PerfilUsuario'

class Curso(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nomCurso = models.CharField(max_length=45)
    desCurso = models.CharField(max_length=120)
    #Etiquetas de los cursos.
    etiqCurso = models.CharField(max_length=120)
    maxAlumnos = models.IntegerField(default=0)
    grupo = models.CharField(max_length=15)
    escuela = models.CharField(max_length=20)
    esEscolar = models.BooleanField(default=False, editable=True)
    costo = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    def __str__(self):
        return self.nomCurso

#class GrupoEscolar(models.Model):
#    idGrupo = models.IntegerField()

class Actividad(models.Model):
    descActividad = models.CharField(max_length=45)
    fechActividad = models.DateTimeField(auto_now_add=True)
    textActividad = models.CharField(max_length=2000)
    nomActividad = models.CharField(max_length=45)

    def __str__(self):
        return self.nomActividad
'''
class Alumno(models.Model):
    idUsuario = PerfilUsuario.user
    idGrupo = Grupo.id
    idAlumno = models.IntegerField()
'''

class Interes(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class OAT(models.Model):
    nomOAT = models.CharField(max_length=45)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    contenido = models.CharField(max_length=2000)
    archivos = models.CharField(max_length=120)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, editable=True,null=True)#, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomOAT
    #man = models.ManyToManyField()


class Multimedia(models.Model):
    imagen = models.ImageField(max_length=None)
    video = models.CharField(max_length=255)#, required=False)
    metadata = models.CharField(max_length=10)
    OAT = models.ForeignKey(OAT, on_delete=models.CASCADE)

    def __str__(self):
        return self.metadata


class Comentario(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    contenido = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.owner +" en"+ self.curso +", a las "+ self.fechaCreacion)

