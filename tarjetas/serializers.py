from rest_framework import serializers

from .models import Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='tipo.nombre')
    marca = serializers.CharField(source='marca.nombre')

    class Meta:
        model = Tarjeta
        fields = ('tipo', 'numero', 'marca')
