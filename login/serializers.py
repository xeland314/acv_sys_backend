"""serializers.py

Este módulo define el serializer PersonaSerializer para serializar
y deserializar instancias del modelo Persona.

Autor: Christopher Villamarín (@xeland314)
Dependencias: django.contrib.auth.models.User,
    rest_framework.serializers,
    .models.Persona,
    .utils.es_una_cedula_valida,
    .utils.es_un_numero_de_telefono_valido
"""

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import Persona
from .exceptions import (
    CedulaInvalida,
    ErrorDeConfirmacionDeContrasena,
    TelefonoInvalido
)
from .utils import (
    es_una_cedula_valida,
    es_un_numero_de_telefono_valido
)

class PersonaSerializer(serializers.ModelSerializer):
    """Serializer para serializar y deserializar instancias del modelo Persona.

    Este serializer hereda de ModelSerializer y define los atributos contrasena y contrasena2 para
    almacenar la contraseña del usuario. También define la clase Meta para especificar el modelo y
    los campos a serializar.

    Atributos:
        - contrasena: Campo para almacenar la contraseña del usuario.
        - contrasena2: Campo para confirmar la contraseña del usuario.
        - Meta: Clase interna para especificar el modelo y los campos a serializar.
    """

    contrasena = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text=_("Contraseña del usuario.")
    )
    contrasena2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text=_("Campo para confirmar la contraseña del usuario.")
    )

    class Meta:
        """Clase interna para especificar el modelo y los campos a serializar.

        Atributos:
            - model: Modelo a serializar.
            - fields: Campos del modelo a serializar.
            - read_only_fields: Campos de solo lectura.
            - default_error_messages: Mensajes de error personalizados.
        """

        model = Persona
        fields = (
            'nombres', 'apellidos', 'cedula', 'email', 'direccion',
            'telefono', 'fecha_nacimiento', 'nivel_educacion',
            'estado_civil', 'contrasena', 'contrasena2', 'fotografia'
        )
        read_only_fields = ('id',)
        default_error_messages = {
            'invalid': _('Datos inválidos.'),
            'required': _('Este campo es obligatorio.'),
        }

    def create(self, validated_data: dict):
        """Crea una nueva instancia del modelo Persona a partir de los datos validados.

        Args:
            validated_data: Diccionario con los datos validados.

        Returns:
            Persona: Nueva instancia del modelo Persona creada a partir de los datos validados.
        """
        password = validated_data.pop('contrasena')
        username = validated_data.get('cedula')
        email = validated_data.get('email')
        user = User.objects.create_user(username, email, password)
        usuario = Persona.objects.create(user=user, **validated_data)
        return usuario

    def validate(self, attrs: dict) -> dict:
        """Valida los datos del serializer.

        Este método verifica si la cédula y el número de teléfono
        son válidos y si las contraseñas coinciden.

        Args:
            attrs: Diccionario con los datos a validar.

        Returns:
            dict: Diccionario con los datos validados.

        Raises:
            serializers.ValidationError: Si la cédula o
            el número de teléfono son inválidos o si las contraseñas no coinciden.
        """

        cedula = attrs.get('cedula')
        if not es_una_cedula_valida(cedula):
            raise CedulaInvalida('Es una cédula inválida.', params={'value': cedula})

        telefono = attrs.get('telefono')
        if not es_un_numero_de_telefono_valido(telefono):
            raise TelefonoInvalido(params={'value': telefono})

        password1 = attrs.get('contrasena')
        password2 = attrs.pop('contrasena2', None)
        if password1 and password1 != password2:
            raise ErrorDeConfirmacionDeContrasena()

        return attrs
