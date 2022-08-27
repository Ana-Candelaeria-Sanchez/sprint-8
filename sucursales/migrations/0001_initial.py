# Generated by Django 4.1 on 2022-08-27 19:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direcciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.OneToOneField(blank=True, db_column='branch_address_id', default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='direcciones.direccion')),
            ],
            options={
                'db_table': 'sucursal',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.DateField(default=datetime.date.today)),
                ('employee_dni', models.PositiveIntegerField(db_column='employee_DNI')),
                ('branch_id', models.ForeignKey(db_column='branch_id', on_delete=django.db.models.deletion.DO_NOTHING, to='sucursales.sucursal')),
            ],
            options={
                'db_table': 'empleado',
            },
        ),
    ]