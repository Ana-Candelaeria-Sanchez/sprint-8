from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TipoCliente(models.Model):
    nombre = models.CharField(max_length=15)

    class Meta:
        db_table = 'TIPO_CLIENTE'

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    id = models.IntegerField(primary_key=True,
                             editable=False,
                             null=False,
                             )
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey('clientes.TipoCliente', default=None, null=True, on_delete=models.CASCADE)
    customer_dni = models.PositiveIntegerField(db_column='customer_DNI')
    dob = models.PositiveIntegerField(blank=True, null=True)
    branch_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'CLIENTE'

    def __str__(self):
        return self.user.username



