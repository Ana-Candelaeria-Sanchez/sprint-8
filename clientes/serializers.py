from django.contrib.auth.models import User
from rest_framework import serializers

from cuentas.serializers import CuentaSerializer
from prestamos.serializers import PrestamoSerializer
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='tipo.nombre')

    class Meta:
        model = Cliente
        fields = ('tipo', 'dni', 'branch')


class UserSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(many=False)
    cuentas = CuentaSerializer(many=True, read_only=True, source='cuenta_set')
    prestamos = PrestamoSerializer(many=True, read_only=True, source='prestamo_set')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'cliente', 'cuentas', 'prestamos']
