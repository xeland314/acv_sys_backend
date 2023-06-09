"""
Módulo de URLs para el control vehicular.

Autor: Christopher Villamarín (@xeland314)
"""

from django.urls import path, include
from rest_framework import routers

from .views import (
    BateriaView, ConductorView, LicenciaView, LlantaView,
    MatriculaView, PropietarioView, VehiculoView
)

router = routers.DefaultRouter()
router.register(r'baterias', BateriaView, basename='baterias')
router.register(r'vehiculos', VehiculoView, basename='vehiculos')
router.register(r'conductores', ConductorView, basename='conductores')
router.register(r'propietarios', PropietarioView, basename='propietarios')
router.register(r'licencias', LicenciaView, basename='licencias')
router.register(r'llantas', LlantaView, basename='llantas')
router.register(r'matriculas', MatriculaView, basename='matriculas')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
