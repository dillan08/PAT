from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from interesesCRUD.serializer import InteresSerializer
from nucleo.models import Interes


# Create your views here.

class InteresVS(viewsets.ModelViewSet):
    serializer_class = InteresSerializer
    queryset = Interes.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

