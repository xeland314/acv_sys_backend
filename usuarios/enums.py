from enum import Enum
from typing import List, Tuple

class EstadoCivil(Enum):
    """
    Clase enumeración para representar los diferentes estados civiles.
    """
    CASADO = "Casado"
    DIVORCIADO = "Divorciado"
    SOLTERO = "Soltero"
    UNION_LIBRE = "Unión Libre"
    VIUDO = "Viudo"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]

class NivelEducacion(Enum):
    """
    Clase enumeración para representar los diferentes niveles de educación.
    """
    GENERAL_BASICA = "General Básica"
    BACHILLERATO = "Bachillerato"
    SUPERIOR = "Superior"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]

class Roles(Enum):
    """
    Clase de enumeración para representar los diferentes roles
    de los usuarios dentro del sistema.
    """
    ADMINISTRADOR = "Administrador"
    CONDUCTOR = "Conductor"
    CONDUCTOR_PROPIETARIO = "Conductor-Propietario"
    ENCARGADO = "Encargado"
    PERSONA_NATURAL = "Persona natural"
    PROPIETARIO = "Propietario"
    RESPONSABLE = "Responsable"
    SECRETARIO = "Secretario"
    SUPERUSER = "Superuser"
    SUPERVISOR = "Supervisor"

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        return [(key.value, key.name) for key in cls]
