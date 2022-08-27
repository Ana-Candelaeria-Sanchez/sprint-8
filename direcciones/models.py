from django.db import models


# Create your models here.

class Direccion(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    customer_id = models.ForeignKey('clientes.Cliente', models.DO_NOTHING, db_column='customer_id', null=True,
                                    default=None)

    class Meta:
        db_table = 'direccion'
