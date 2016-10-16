from rest_framework import serializers
from nucleo.models import OAT


class OATSerializer(serializers.ModelSerializer):
    fechaCreacion = serializers.DateTimeField(required=False)

    class Meta:
        model = OAT
        fields = (
            'pk',
            'nomOAT',
            'fechaCreacion',
            'contenido',
            'archivos',
            'owner',
            'curso',
        )

    def create(self, validated_data):
        return OAT.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomOAT = validated_data.get('nomOAT', instance.nomOAT)
        instance.descOAT = validated_data.get('descOAT', instance.descOAT)
        instance.fechaCreacion = validated_data.get('fechaCreacion', instance.fechaCreacion)
        instance.contenido = validated_data.get('contenido', instance.contenido)
        instance.archivos = validated_data.get('archivos', instance.archivos)
        instance.curso = validated_data.get('curso', instance.curso)
        instance.save()
        return instance
