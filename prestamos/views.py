from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Prestamo
from .serializers import PrestamoSerializer


# Create your views here.
class PrestamoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        permission_classes = [IsAuthenticated, IsAdminUser]
        queryset = Prestamo.objects.all()
        serializer = PrestamoSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def me(self, request):
        user = request.user
        serializer = PrestamoSerializer(user.prestamo_set, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
