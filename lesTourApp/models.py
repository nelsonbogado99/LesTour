from django.db import models

#tabla para registrar empleados
class Empleados(models.Model):
    ci_numero=models.IntegerField()
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()

#tabla para registrar clientes
class Clientes(models.Model):
    ci_numero=models.IntegerField()
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()

#tabla para registrar hoteles
class Hoteles(models.Model):
    nombre=models.CharField(max_length=200)
    ciudad=models.CharField(max_length=200)
    barrio=models.CharField(max_length=200)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    email=models.CharField(max_length=100)
    pisos=models.IntegerField()
    habitaciones=models.IntegerField()
    
#tabla para registrar los tipos de habitaciones
class Tipo_Habitacion(models.Model):
    nombre=models.CharField(max_length=100)
    capacidad=models.IntegerField()
    costo=models.IntegerField()

#tabla para registrar las areas o departamentos dentro del hotel
class Areas(models.Model):
    nombre=models.CharField(max_length=100)

#tabla para registrar los cargos que se encuentran en cada area
class Cargo(models.Model):
    nombre=models.CharField(max_length=100)
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE)

class Puesto_Trabajo(models.Model):
    nombre=models.CharField(max_length=100)
    id_empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE)
    id_cargo=models.ForeignKey(Cargo, on_delete=models.CASCADE)