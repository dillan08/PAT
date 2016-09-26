from rest_framework import serializers
from nucleo.models import Curso


class cursoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    nomCurso = serializers.CharField(max_length=45)
    desCurso = serializers.CharField(max_length=120)
    etiqCurso = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Curso.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomCurso = validated_data.get('nomCurso', instance.nomCurso)
        instance.desCurso = validated_data.get('desCurso', instance.desCurso)
        instance.etiqCurso = validated_data.get('etiqCurso', instance.etiqCurso)
        instance.save()
        return instance