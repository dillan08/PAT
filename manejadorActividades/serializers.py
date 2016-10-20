from rest_framework import serializers
from nucleo.models import Actividad
from manejadorCursos.serializers import cursoSerializer
# calificacion = models.IntegerField(default=0)
# tipo = models.CharField(max_length=2, choices=ACTIVIDAD_CHOICES)
# cursos = models.ManyToManyField(Curso)

class actividadesSerializer(serializers.ModelSerializer):
    #cursos = cursoSerializer(read_only=True, many=True, required=False)
    #cursos = cursoSerializer(many=True)
    class Meta:
        model = Actividad
        fields = '__all__'

    def create(self, validated_data):
        return Actividad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.calificacion = validated_data.get('calificacion', instance.calificacion)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.cursos = validated_data.get('cursos', instance.cursos)
        instance.save()
        return instance

