import datetime

from django.db import models


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.OneToOneField('direcciones.Direccion', models.DO_NOTHING, db_column='branch_address_id',
                                             blank=True, null=True, default=None)

    class Meta:
        db_table = 'sucursal'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.DateField(default=datetime.date.today)
    employee_dni = models.PositiveIntegerField(db_column='employee_DNI')
    branch_id = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='branch_id')

    class Meta:
        db_table = 'empleado'
