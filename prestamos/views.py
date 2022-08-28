from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from sucursales.views import es_cliente
from .models import Prestamo
from .serializers import PrestamoSerializer


# Create your views here.
class PrestamoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Prestamo.objects.all().order_by('-id')
    serializer_class = PrestamoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user: User = request.user

        if es_cliente(user):
            return Response(
                self.get_serializer(
                    self.queryset.filter(cliente_id=user.id),
                    many=True).data,
                status=HTTP_200_OK)
        else:
            return super().list(request)

    @action(methods=['get'], detail=False)
    def me(self, request):
        user = request.user
        serializer = PrestamoSerializer(user.prestamo_set, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):

        if es_cliente(request.user):
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = PrestamoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_200_OK)

    def destroy(self, request, pk=None):
        if es_cliente(request.user):
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, pk)
