from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from manejadorComentarios.serializers import ComentarioSerializer
from nucleo.models import Comentario
# Create your views here.

class ComentariosVS(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)