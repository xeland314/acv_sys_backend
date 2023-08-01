# Generated by Django 4.2.1 on 2023-08-01 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anticipo_alertas', models.DecimalField(decimal_places=2, help_text='Usando este valor es posible anticipar los mantenimientos con anticipación.', max_digits=10, verbose_name='Anticipo alertas')),
                ('frecuencia_minima', models.DecimalField(decimal_places=2, help_text='El kilometraje/tiempo mínimo en el que se deben realizar las operaciones.', max_digits=10, verbose_name='Frecuencia mínima')),
                ('final_ciclo', models.DecimalField(decimal_places=2, help_text='El kilometraje/tiempo límite que marca el fin de cada ciclo de mantenimiento.', max_digits=10, verbose_name='Final de ciclo de mantenimiento')),
                ('unidad', models.CharField(choices=[('km', 'KILOMETROS'), ('mi', 'MILLAS'), ('días', 'DIAS'), ('semanas', 'SEMANAS'), ('meses', 'MESES')], help_text='La unidad de medida del kilometraje.', max_length=10, verbose_name='Unidad')),
                ('vehiculo', models.OneToOneField(help_text='El vehículo al que pertenece el manual de mantenimiento.', on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
            options={
                'verbose_name': 'Manual de mantenimiento',
                'verbose_name_plural': 'Manuales de mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='El sistema del vehículo.', max_length=50, verbose_name='Sistema')),
                ('manual_mantenimiento', models.ForeignKey(help_text='Manual de mantenimiento a la que pertenece este sistema.', on_delete=django.db.models.deletion.CASCADE, related_name='sistemas_vehiculos', to='manual_de_mantenimiento.manualmantenimiento')),
            ],
            options={
                'verbose_name': 'Sistema del vehículo',
                'verbose_name_plural': 'Sistemas del vehículo',
            },
        ),
        migrations.CreateModel(
            name='Subsistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='El sub-sistema del vehículo al que pertenece la operación.', max_length=50, verbose_name='Sub-sistema')),
                ('sistema', models.ForeignKey(help_text='Subsistema del sistema principal del vehículo.', on_delete=django.db.models.deletion.CASCADE, related_name='subsistemas_vehiculos', to='manual_de_mantenimiento.sistema')),
            ],
            options={
                'verbose_name': 'Subsistema del vehículo',
                'verbose_name_plural': 'Subsistemas del vehículo',
            },
        ),
        migrations.CreateModel(
            name='OperacionMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(choices=[('I', 'INSPECCIONAR'), ('A', 'AJUSTAR'), ('R', 'REEMPLAZAR'), ('T', 'TORQUE'), ('L', 'LUBRICAR')], help_text='La tarea a realizar en la operación.', max_length=50, verbose_name='Tarea')),
                ('descripcion', models.TextField(blank=True, help_text='Descripción de la tarea a realizar', verbose_name='Descripción')),
                ('frecuencia', models.DecimalField(decimal_places=2, help_text='El kilometraje/tiempo en el que se debe realizar la operación.', max_digits=10, verbose_name='Frecuencia')),
                ('unidad', models.CharField(choices=[('km', 'KILOMETROS'), ('mi', 'MILLAS'), ('días', 'DIAS'), ('semanas', 'SEMANAS'), ('meses', 'MESES')], help_text='La unidad de medida del kilometraje.', max_length=10, verbose_name='Unidad')),
                ('subsistema', models.ForeignKey(help_text='Operación de mantenimiento que se debe realizar en un vehículo.', on_delete=django.db.models.deletion.CASCADE, related_name='operaciones_mantenimiento', to='manual_de_mantenimiento.subsistema')),
            ],
            options={
                'verbose_name': 'Operación de mantenimiento',
                'verbose_name_plural': 'Operaciones de mantenimiento',
            },
        ),
    ]
