# Generated by Django 4.2.1 on 2023-05-14 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_vehicular', '0002_propietario_vehiculo_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='propietario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control_vehicular.propietario'),
        ),
    ]
