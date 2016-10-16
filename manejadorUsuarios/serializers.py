from nucleo.models import PerfilUsuario
from rest_framework import serializers
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email',"password",'pk',)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class PerfilSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer()
    class Meta:
        model = PerfilUsuario
        fields = ('nivelEstudios','user','pk',)

    def update(self, instance, validated_data):
        user_Data = validated_data.pop('user')
        myUser = instance.user
        instance.nivelEstudios = validated_data.get('nivelEstudios',instance.nivelEstudios)
        instance.save()
        myUser.email = user_Data.get('email', myUser.email)
        myUser.password = user_Data.get('password', myUser.password)
        myUser.save()
        return instance

    def create(self, validated_data):
        datos_user = validated_data.pop('user')
        user = User.objects.create(**datos_user)
        perfil = PerfilUsuario.objects.create(user=user, **validated_data)
        return perfil
        #datos_perfil = validated_data.pop('perfil')
        #user = User.objects.create(**validated_data)
        #PerfilUsuario.objects.create(user=user, **datos_perfil)
        #return user

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
        fields = ('username', 'password', 'email','perfil',)

    def create(self, validated_data):
        datos_perfil = validated_data.pop('perfil')
        user = User.objects.create(**validated_data)
        PerfilUsuario.objects.create(user=user, **datos_perfil)
        return user

    def update(self, instance, validated_data):
        perfilData = validated_data.pop('perfil')
        perfil = instance.perfil
        perfil.tipo = perfilData.get('tipo', perfil.tipo)
        perfil.save()
        return instance