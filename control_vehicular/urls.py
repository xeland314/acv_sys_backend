from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import VehiculoView

router = routers.DefaultRouter()
router.register(r"vehiculos", VehiculoView, "vehiculos")

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Vehiculos API')),
]
