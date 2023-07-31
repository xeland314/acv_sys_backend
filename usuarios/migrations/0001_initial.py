# Generated by Django 4.2.1 on 2023-07-30 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import usuarios.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Administrador', 'ADMINISTRADOR'), ('Conductor', 'CONDUCTOR'), ('Conductor-Propietario', 'CONDUCTOR_PROPIETARIO'), ('Encargado', 'ENCARGADO'), ('Persona natural', 'PERSONA_NATURAL'), ('Propietario', 'PROPIETARIO'), ('Secretario', 'SECRETARIO'), ('Superuser', 'SUPERUSER'), ('Supervisor', 'SUPERVISOR')], help_text='Rol de un usuario en el sistema.', max_length=30, verbose_name='Rol')),
                ('cedula', models.CharField(help_text='Cédula de la persona.', max_length=10, validators=[usuarios.validators.validar_cedula], verbose_name='Cédula')),
                ('email', models.EmailField(help_text='Email de la persona.', max_length=127, verbose_name='Email')),
                ('telefono', models.CharField(help_text='Teléfono de la persona.', max_length=13, validators=[usuarios.validators.validar_numero_de_telefono], verbose_name='Teléfono')),
                ('direccion', models.TextField(blank=True, help_text='Dirección de la persona.', verbose_name='Dirección')),
                ('fecha_nacimiento', models.DateField(help_text='Fecha de nacimiento de la persona.', validators=[usuarios.validators.validar_fecha_de_nacimiento], verbose_name='Fecha de nacimiento')),
                ('nivel_educacion', models.CharField(choices=[('General Básica', 'GENERAL_BASICA'), ('Bachillerato', 'BACHILLERATO'), ('Superior', 'SUPERIOR')], help_text='Nivel de educación de la persona.', max_length=30, verbose_name='Nivel de educación')),
                ('estado_civil', models.CharField(choices=[('Casado', 'CASADO'), ('Divorciado', 'DIVORCIADO'), ('Soltero', 'SOLTERO'), ('Unión Libre', 'UNION_LIBRE'), ('Viudo', 'VIUDO')], help_text='Estado civil de la persona.', max_length=20, verbose_name='Estado Civil')),
                ('fotografia', models.ImageField(blank=True, help_text='Fotografía opcional de la persona.', null=True, upload_to='', verbose_name='Fotografía')),
                ('empresa', models.ForeignKey(help_text='Empresa en la que labora el trabajador.', on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='empresas.empresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de usuario',
                'verbose_name_plural': 'Perfiles de usuario',
            },
        ),
    ]
