"""urls.py

Define los patrones de URL para la API de PerfilUsuario.

Autor: Christopher Villamarín (@xeland314)
"""
from django.urls import path, include
from rest_framework import routers
from .views import PerfilView

router = routers.DefaultRouter()
router.register(r"perfiles", PerfilView, basename="perfiles")

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
