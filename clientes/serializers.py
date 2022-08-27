from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='tipo.nombre')

    class Meta:
        model = Cliente
        fields = ('tipo', 'dni', 'branch')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    cliente = ClienteSerializer(many=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'cliente']
