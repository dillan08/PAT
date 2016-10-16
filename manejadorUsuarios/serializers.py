from rest_framework.exceptions import ValidationError

from nucleo.models import PerfilUsuario
from rest_framework import serializers
from django.contrib.auth.models import User, Group


#from rest_auth.serializers import UserDetailsSerializer

class UsuarioSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, style={'input_type':'password'}, write_only=True, required=False)
    email = serializers.EmailField(required=False)
    role = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            "password",
            'role'
        )

    def validate(self, attrs):
        try:
            Group.objects.get(pk=attrs['role'])
        except Group.DoesNotExist:
            raise ValidationError({'message': 'El rol no existe'})
        except KeyError:
            pass
        return attrs

class PerfilSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(many=False, required=False)
    #nivelEstudios = serializers.SerializerMethodField()
    imagen = serializers.ImageField(required=False, use_url=True, max_length=None)
    class Meta:
        model = PerfilUsuario
        fields = (
            'id',
            'user',
            'nivelEstudios',
            'descripcion',
            'imagen'
        )

    def get_nivelEstudios(self, obj):
        return obj.get_nivelEstudios_dysplay()

    def create(self, validated_data):
        datos_user = validated_data.pop('user')
        user_dict = {
            'username': datos_user['username'],
            'password': datos_user['password'],
            'email': datos_user['email'],
        }
        user = User.objects.create_user(**user_dict)
        user.groups.add(datos_user['role'])
        if user.groups.filter(name__contains='Administrador').count() > 0:
            user.is_staff=True
            user.save()
        validated_data['user']=user

        return PerfilUsuario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        try:
            user_Data = validated_data.pop('user')
        except:
            print("No existe elemento usuario")
        instance.nivelEstudios = validated_data.get('nivelEstudios',instance.nivelEstudios)
        instance.descripcion = validated_data.get('descripcion',instance.descripcion)
        try:
            instance.imagen = validated_data.get('imagen', instance.imagen)
        except:
            print("No contiene imagen")
        instance.save()
        return instance




#class UserSerializer(UserDetailsSerializer):

#    nivelEstudios = serializers.CharField(source="perfilusuario.nivelEstudios")

#    class Meta(UserDetailsSerializer.Meta):
#        fields = UserDetailsSerializer.Meta.fields + ('nivelEstudios',)

#    def create(self, validated_data):
#        datos_user = validated_data.pop('user')
#        user = User.objects.create(**datos_user)
#        return PerfilUsuario.objects.create(user=user, **validated_data)

#    def update(self, instance, validated_data):
#        profile_data = validated_data.pop('perfilusuario', {})
#        nivelEstudios = profile_data.get('nivelEstudios')

#        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
 #       profile = instance.perfilusuario
 #       if profile_data and nivelEstudios:
 #           profile.nivelEstudios = nivelEstudios
 #           profile.save()
 #       return instance
