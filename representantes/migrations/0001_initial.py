# Generated by Django 4.2.1 on 2023-08-01 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('perfilusuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.perfilusuario')),
                ('ruc', models.CharField(help_text='RUC del representante.', max_length=13, verbose_name='RUC')),
            ],
            options={
                'verbose_name': 'Representante',
                'verbose_name_plural': 'Representantes',
            },
            bases=('usuarios.perfilusuario',),
        ),
    ]
