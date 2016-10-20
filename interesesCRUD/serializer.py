from rest_framework import serializers
from nucleo.models import Interes


class InteresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interes
        fields = ('nombre',)

    def create(self, validated_data):
        return Interes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.save()
        return instance
