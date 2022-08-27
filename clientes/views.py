from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from tarjetas.serializers import TarjetaSerializer
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        permission_classes = [IsAdminUser]
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def cards(self, request, pk=None):

        try:
            user = User.objects.get(username=pk)
        except User.DoesNotExist:
            return Response(status=404)

        serializer = TarjetaSerializer(user.cliente.tarjeta_set.filter(tipo=1), many=True)
        return Response(serializer.data, status=HTTP_200_OK)
