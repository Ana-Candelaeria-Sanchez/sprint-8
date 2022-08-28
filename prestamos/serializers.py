from rest_framework import serializers

from .models import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='tipo.nombre', read_only=True)
    cliente_id = serializers.IntegerField(write_only=True, min_value=1)
    tipo_id = serializers.IntegerField(write_only=True, min_value=1)

    class Meta:
        model = Prestamo
        fields = ('tipo', 'tipo_id', 'cliente_id', 'total',)

    def save(self, **kwargs):
        tipo = self.validated_data.get('tipo_id')
        cliente = self.validated_data.get('cliente_id')
        total = self.validated_data.get('total')
        return Prestamo.objects.create(tipo_id=tipo, cliente_id=cliente, total=total)
