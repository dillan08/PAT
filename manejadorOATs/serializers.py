from rest_framework import serializers
from nucleo.models import OAT


class OATSerializer(serializers.ModelSerializer):
    fechaCreacion = serializers.DateTimeField(required=False)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = OAT
        fields = '__all__'

    def create(self, validated_data):
        return OAT.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomOAT = validated_data.get('nomOAT', instance.nomOAT)
        #instance.descOAT = validated_data.get('descOAT', instance.descOAT)
        instance.fechaCreacion = validated_data.get('fechaCreacion', instance.fechaCreacion)
        instance.contenido = validated_data.get('contenido', instance.contenido)
        instance.archivos = validated_data.get('archivos', instance.archivos)
        #instance.curso = validated_data.get('curso', instance.curso)
        instance.save()
        return instance


# nomOAT = models.CharField(max_length=45)
# fechaCreacion = models.DateTimeField(auto_now_add=True)
# contenido = models.CharField(max_length=2000)
# archivos = models.CharField(max_length=120)
# owner = models.ForeignKey(
