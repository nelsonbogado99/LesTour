from django.contrib import admin
from . import models

admin.site.register(models.Empleados)
admin.site.register(models.Clientes)
admin.site.register(models.Reservas)
admin.site.register(models.Hoteles)
admin.site.register(models.Habitacion)
admin.site.register(models.Tipo_Habitacion)
admin.site.register(models.Reserva_Huesped)
admin.site.register(models.Puesto_Trabajo)
admin.site.register(models.Cargo)
admin.site.register(models.Areas)