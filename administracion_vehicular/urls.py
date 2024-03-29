"""administracion_vehicular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api_generate_token/', views.obtain_auth_token),
    path('dashboard/', admin.site.urls),
    path('docs/', include_docs_urls(title='Developer API documentation')),
    path('', include('empresas.urls')),
    path('', include('manual_de_mantenimiento.urls')),
    path('', include('ordenes_de_mantenimiento.urls')),
    path('', include('ordenes_de_trabajo.urls')),
    path('', include('representantes.urls')),
    path('', include('usuarios.urls')),
    path('', include('vehiculos.urls')),
]
