from nucleo.models import OAT
from manejadorOATs.serializers import OATSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from nucleo.permissions import IsOwnerOrReadOnly


class OATsViewSet(viewsets.ModelViewSet):
    serializer_class = OATSerializer
    queryset = OAT.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        # def check_object_permissions(self, request, obj):


        # class OATList(APIView):
        #     def get(self, request, format=None):
        #         oats = OAT.objects.all()
        #         serializer = OATSerializer(oats, many=True)
        #         return Response(serializer.data)
        #
        #     def post(self, request, format=None):
        #         serializer = OATSerializer(data=request.data)
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data, status=status.HTTP_201_CREATED)
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        #
        # class OATDetail(APIView):
        #
        #     def get_objects(self, pk):
        #         try:
        #             return OAT.objects.get(pk=pk)
        #         except OAT.DoesNotExist:
        #             raise Http404
        #
        #     def get(self, request, pk, format=None):
        #         oat = self.get_objects(pk=pk)
        #         serializer = OATSerializer(oat)
        #         return Response(serializer.data)
        #
        #     def put(self, request, pk, format=None):
        #         oat = self.get_objects(pk)
        #         serializer = OATSerializer(oat, data=request.data, partial=True)
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(serializer.data, status=status.HTTP_201_CREATED)
        #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        #     def delete(self, request, pk, format=None):
        #         oat = self.get_object(pk)
        #         oat.delete()
        #         return Response(status=status.HTTP_204_NO_CONTENT)
