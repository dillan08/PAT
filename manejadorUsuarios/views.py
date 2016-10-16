from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from manejadorUsuarios.serializers import PerfilSerializer
from nucleo.models import PerfilUsuario, User

class PerfilAdministrador(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = PerfilUsuario.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
        perfil = self.get_object(pk)
        serializer = PerfilSerializer(perfil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        #perfil = self.get_object(pk=pk)
        try:
            user = User.objects.get(pk)
        except User.DoesNotExist:
            raise Http404
        user.delete()
        #perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


