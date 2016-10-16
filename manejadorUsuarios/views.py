from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from manejadorUsuarios.serializers import PerfilUsuarioSerializer, UserSerializer, PerfilSerializer
from nucleo.models import PerfilUsuario, User

# Create your views here.
class PerfilDetail(APIView):
    def get_object(self, pk):
        try:
            return PerfilUsuario.objects.get(pk=pk)
        except PerfilUsuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = PerfilSerializer(perfil)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        #user_data = request.data.pop("user")
        perfil = self.get_object(pk=pk)
        serializer = PerfilSerializer(perfil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        #perfil = self.get_object(pk=pk)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        user.delete()
        #perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PerfilList(APIView):
    #Obtener listado de usuarios
    def get(self, request, format=None):
        perfiles = PerfilUsuario.objects.all()
        serializer = PerfilSerializer(perfiles, many=True)
        return Response(serializer.data)
    #Crear usuario
    def post(self, request, format=None):
        #print(request.data)
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def put(self, request, format=None):
#        user = User()
#        serializer = UserSerializer(user, data=request.data, partial=True)
#        if serializer.is_valid():
#            serializer.save()
#            #serializer.update(PerfilUsuario.objects.get(user.username=user.username))
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST