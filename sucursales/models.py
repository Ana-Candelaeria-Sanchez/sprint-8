import datetime

from django.db import models


class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.BinaryField()
    name = models.TextField()
    address = models.OneToOneField('direcciones.Direccion', models.DO_NOTHING, db_column='address_id',
                                   blank=True, null=True, default=None)

    class Meta:
        db_table = 'sucursal'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    hire_date = models.DateField(default=datetime.date.today, null=True)
    dni = models.PositiveIntegerField(db_column='employee_DNI')
    branch = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='branch_id')

    class Meta:
        db_table = 'empleado'
