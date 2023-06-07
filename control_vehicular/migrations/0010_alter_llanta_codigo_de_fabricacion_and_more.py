# Generated by Django 4.2.1 on 2023-06-07 18:02

import control_vehicular.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_vehicular', '0009_alter_bateria_codigo_de_fabricacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llanta',
            name='codigo_de_fabricacion',
            field=models.CharField(help_text='El código de fabricación de la llanta.', max_length=50, validators=[control_vehicular.models.validar_codigo_dot], verbose_name='Código de fabricación'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(help_text='La placa del vehículo.', max_length=10, unique=True, validators=[control_vehicular.models.validar_placa_vehicular], verbose_name='Placa'),
        ),
    ]
