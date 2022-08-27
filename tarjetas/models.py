from django.db import models


# Create your models here.
class TipoTarjeta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_tarjeta'


class MarcaTarjeta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'marca_tarjeta'


class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(TipoTarjeta, on_delete=models.DO_NOTHING, default=None, null=True)
    marca = models.ForeignKey(MarcaTarjeta, on_delete=models.DO_NOTHING, default=None, null=True)
    numero = models.CharField(max_length=20)
    cvv = models.CharField(max_length=3)
    fecha_de_otorgamiento = models.DateField(null=True)
    fecha_de_expiracion = models.DateField(null=True)
    customer_id = models.ForeignKey(
        'clientes.Cliente', models.DO_NOTHING, db_column='customer_id')

    class Meta:
        db_table = 'tarjeta'
