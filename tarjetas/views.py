from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Tarjeta
from .serializers import TarjetaSerializer


# Create your views here.
class TarjetaViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        permission_classes = [IsAuthenticated, IsAdminUser]
        queryset = Tarjeta.objects.all()
        serializer = TarjetaSerializer(queryset, many=True)
        return Response(serializer.data)
