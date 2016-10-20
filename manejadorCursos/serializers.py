from rest_framework import serializers
from nucleo.models import Curso


class cursoSerializer(serializers.ModelSerializer):
    #oats = serializers.ManyToManyField()
    class Meta:
        model = Curso
        fields = '__all__'


    def update(self, instance, validated_data):
        instance.nomCurso = validated_data.get('nomCurso', instance.nomCurso)
        instance.desCurso = validated_data.get('desCurso', instance.desCurso)
        instance.etiqCurso = validated_data.get('etiqCurso', instance.etiqCurso)
        instance.maxAlumnos = validated_data.get('maxAlumnos', instance.maxAlumnos)
        instance.grupo = validated_data.get('grupo', instance.grupo)
        instance.escuela = validated_data.get('escuela', instance.escuela)
        instance.esEscolar = validated_data.get('esEscolar', instance.esEscolar)
        instance.costo = validated_data.get('costo', instance.costo)
        instance.save()
        return instance
