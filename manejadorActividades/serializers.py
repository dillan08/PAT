from rest_framework import serializers
from nucleo.models import Actividad


class actividadesSerializer(serializers.ModelSerializer):
    fechActividad = serializers.DateTimeField(required=False)

    class Meta:
        model = Actividad
        fields = (
            'pk',
            'descActividad',
            'fechActividad',
            'textActividad',
            'nomActividad',
        )

    def create(self, validated_data):
        return Actividad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.descActividad = validated_data.get('descActividad', instance.descActividad)
        instance.fechActividad = validated_data.get('fechActividad', instance.fechActividad)
        instance.textActividad = validated_data.get('textActividad', instance.textActividad)
        instance.nomActividad = validated_data.get('nomActividad', instance.nomActividad)
        instance.save()
        return instance

