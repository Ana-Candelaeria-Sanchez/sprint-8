from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sucursales.views import es_cliente
from .models import Direccion
from .serializers import DireccionSerializer


# Create your views here.
class DireccionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Direccion.objects.all().order_by('-id')
    serializer_class = DireccionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, pk=None, *args, **kwargs):
        user: User = request.user
        if es_cliente(user):
            try:
                direccion: Direccion = Direccion.objects.get(pk=pk)
                if direccion.customer_id.user == user:
                    return super().update(request, pk, *args, **kwargs)
                else:
                    return Response(status=status.HTTP_403_FORBIDDEN)
            except Direccion.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            return super().update(request, pk, *args, **kwargs)

    def create(self, request):
        if es_cliente(request.user):
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            return super().create(request)
