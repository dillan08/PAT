from rest_framework import serializers
from nucleo.models import Curso


class cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'pk',
            'owner',
            'nomCurso',
            'desCurso',
            'etiqCurso',
            'maxAlumnos',
        )

    def create(self, validated_data):
        return Curso.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomCurso = validated_data.get('nomCurso', instance.nomCurso)
        instance.desCurso = validated_data.get('desCurso', instance.desCurso)
        instance.etiqCurso = validated_data.get('etiqCurso', instance.etiqCurso)
        instance.maxAlumnos = validated_data.get('maxAlumnos', instance.maxAlumnos)
        instance.save()
        return instance
