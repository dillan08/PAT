from rest_framework import serializers
from nucleo.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    fechaCreacion = serializers.DateTimeField(required=False)
    class Meta:
        model = Comentario
        fields = '__all__'

    def create(self, validated_data):
        return Comentario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.contenido = validated_data.get('contenido', instance.contenido)
        instance.save()
        return instance