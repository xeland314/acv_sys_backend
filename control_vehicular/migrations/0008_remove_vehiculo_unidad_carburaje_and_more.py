# Generated by Django 4.2.1 on 2023-06-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_vehicular', '0007_alter_conductor_options_alter_licencia_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='unidad_carburaje',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='unidad_carburante',
            field=models.FloatField(default=0.1, verbose_name='Unidad carburante'),
            preserve_default=False,
        ),
    ]
