# Generated by Django 4.2.1 on 2023-06-13 15:56

from django.db import migrations, models
import django.db.models.deletion
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_persona_apellidos_alter_persona_cedula_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comercial', models.CharField(help_text='Nombre comercial de la empresa.', max_length=150, verbose_name='Nombre comercial')),
                ('ruc', models.CharField(help_text='RUC de la empresa.', max_length=13, verbose_name='RUC')),
                ('direccion', models.CharField(help_text='Dirección de la empresa.', max_length=200, verbose_name='Dirección')),
                ('correo', models.EmailField(help_text='Correo electrónico de la empresa.', max_length=100, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(help_text='Teléfono de la empresa.', max_length=15, validators=[login.models.validar_numero_de_telefono], verbose_name='Teléfono')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.persona')),
                ('ruc', models.CharField(help_text='RUC del representante.', max_length=13, verbose_name='RUC')),
            ],
            bases=('login.persona',),
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.persona')),
                ('empresa', models.ForeignKey(help_text='Empresa a la que está asociado el trabajador.', on_delete=django.db.models.deletion.PROTECT, to='login.empresa')),
            ],
            bases=('login.persona',),
        ),
        migrations.AddField(
            model_name='empresa',
            name='representante_legal',
            field=models.OneToOneField(help_text='Representante legal de la empresa.', on_delete=django.db.models.deletion.CASCADE, to='login.representante'),
        ),
    ]