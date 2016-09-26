from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from nucleo.models import Curso
from manejadorCursos.serializers import cursoSerializer

class CursosList(APIView):
    def get(self, request, format=None):
        cursos = Curso.objects.all()
        serializer = cursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = cursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoDetail(APIView):
    def get_objects(self, pk):
        try:
            return Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        curso = self.get_objects(pk=pk)
        serializer = cursoSerializer(curso)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        curso = self.get_object(pk)
        serializer = cursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        curso = self.get_object(pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)