from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from nucleo.models import Actividad
from manejadorActividades.serializers import actividadesSerializer

from rest_framework import viewsets
from rest_framework.response import Response
#from rest_framework import status


class ActividadVS(viewsets.ModelViewSet):
    serializer_class = actividadesSerializer
    queryset=Actividad.objects.all()

    def create(self, request, *args, **kwargs):
        #print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
# class ActividadList(APIView):
#     def get(self, request, format=None):
#         actividad = Actividad.objects.all()
#         serializer = actividadesSerializer(actividad, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = actividadesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ActividadDetail(APIView):
#
#     def get_objects(self, pk):
#         try:
#             return Actividad.objects.get(pk=pk)
#         except Actividad.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         actividad = self.get_objects(pk=pk)
#         serializer = actividadesSerializer(actividad)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         actividad = self.get_objects(pk=pk)
#         serializer = actividadesSerializer(actividad, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         curso = self.get_object(pk)
#         curso.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#    def update(self, request, *args, **kwargs):
#        data = request.DATA
#        actividad = self.get_objects(data.pk)
#        serializer = actividadesSerializer(actividad, data=data, partial=True)

#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status.HTTP_201_CREATED)
#        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
