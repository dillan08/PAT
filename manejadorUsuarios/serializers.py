from nucleo.models import PerfilUsuario
from rest_framework import serializers
from django.contrib.auth.models import User


# serializer = usuarioSerializer(data={'username':'user1', 'email':'user1@mail.com', 'password':'123456asd', 'first_name':'Dillan', 'last_name':'Barbosa','nivelEstudios':'Media Superior'})
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    nivelEstudios = serializers.CharField( max_length=30)
    class Meta:
        model = PerfilUsuario
        fields = ( 'nivelEstudios',)



class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilUsuarioSerializer()
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        datos_perfil = validated_data.pop('perfil')
        user = User.objects.create(**validated_data)
        PerfilUsuario.objects.create(user=user, **datos_perfil)
        return user
