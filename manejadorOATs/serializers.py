from rest_framework import serializers
from nucleo.models import OAT

class OATSerializer(serializers.ModelSerializer):
    class Meta():
        model = OAT
        fields = ('nomOAT','descOAT','textOAT',)

    def create(self, validated_data):
        oat = OAT.objects.create(**validated_data)
        return oat

    def update(self, instance, validated_data):
        instance.nomOAT = validated_data.get('nomOAT', instance.nomOAT)
        instance.descOAT = validated_data.get('decOAT', instance.descOAT)
        instance.textOAT = validated_data.get('textOAT', instance.textOAT)
        instance.save()
        return instance
