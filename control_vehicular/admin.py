from django.contrib import admin

from .models import (
    Bateria, Conductor, Licencia, Llanta,
    Matricula, Propietario, Vehiculo
)

admin.site.register(Bateria)
admin.site.register(Conductor)
admin.site.register(Licencia)
admin.site.register(Llanta)
admin.site.register(Matricula)
admin.site.register(Propietario)
admin.site.register(Vehiculo)
