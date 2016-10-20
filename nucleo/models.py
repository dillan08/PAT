from django.db import models
from django.contrib.auth.models import User

#class User()...
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


class OAT(models.Model):
    nomOAT = models.CharField(max_length=45)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    contenido = models.CharField(max_length=2000)
    archivos = models.CharField(max_length=120)     #<-----------Ya hay que irlo quitando.
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    pass

    def __str__(self):
        return self.nomOAT


class Curso(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nomCurso = models.CharField(max_length=45)
    desCurso = models.CharField(max_length=120)
    #Etiquetas de los cursos.
    etiqCurso = models.CharField(max_length=120)#<---------------------modificar
    maxAlumnos = models.IntegerField(default=0)
    grupo = models.CharField(max_length=15)
    escuela = models.CharField(max_length=20)
    esEscolar = models.BooleanField(default=False, editable=True)
    costo = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    oats = models.ManyToManyField(
        OAT,
        related_name='Curso_has_OAT'
    )
    usuarios = models.ManyToManyField(
        'auth.User',
        related_name='Curso_has_User'
    )
    pass
    def __str__(self):
        return self.nomCurso


class Interes(models.Model):
    nombre = models.CharField(max_length=20)
    cursos = models.ManyToManyField(
        Curso,
        related_name='Curso_Has_Inter',
    )
    class Meta:
        ordering = ('nombre',)
    def __str__(self):
        return self.nombre


class Multimedia(models.Model):
    imagen = models.ImageField(max_length=None)
    video = models.CharField(max_length=255)#, required=False)
    metadata = models.CharField(max_length=10)
    oats = models.ForeignKey(OAT, on_delete=models.CASCADE)

    def __str__(self):
        return self.metadata


class Comentario(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    contenido = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=False
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str(self.owner +" en"+ self.curso +", a las "+ self.fechaCreacion)


class Actividad(models.Model):
    ACTIVIDAD_CHOICES=(
        ('JU','JUEGO'),
        ('EX','EXAMEN'),
    )
    calificacion = models.IntegerField(default=0)
    tipo = models.CharField(max_length=2, choices=ACTIVIDAD_CHOICES)
    cursos = models.ManyToManyField(Curso, related_name="Cur_has_Act")

    def __str__(self):
        return str("Tu calificacion es: "+ str(self.calificacion))

