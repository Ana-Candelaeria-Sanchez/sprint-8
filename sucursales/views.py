from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from prestamos.models import Prestamo
from prestamos.serializers import PrestamoSerializer
from .models import Sucursal
from .serializers import SucursalSerializer


class SucursalViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = Sucursal.objects.all()
        serializer = SucursalSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def loans(self, request, pk=None):

        try:
            user = Sucursal.objects.get(pk=pk)
        except Sucursal.DoesNotExist:
            return Response(status=404)

        prestamos = Prestamo.objects.filter(cliente__cliente__branch_id=pk)
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
