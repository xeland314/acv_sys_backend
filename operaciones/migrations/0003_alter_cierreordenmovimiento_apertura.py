# Generated by Django 4.2.1 on 2023-06-07 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0002_aperturaordenmovimiento_cierreordenmovimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cierreordenmovimiento',
            name='apertura',
            field=models.OneToOneField(help_text='Apertura de la orden de movimiento a la que se vincula el cierre de la misma', on_delete=django.db.models.deletion.PROTECT, to='operaciones.aperturaordenmovimiento'),
        ),
    ]
