from rest_framework import serializers

from .models import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='tipo.nombre')

    class Meta:
        model = Prestamo
        fields = ('tipo', 'total')
