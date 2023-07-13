from django.db import models

# tabla para registrar las ciudades de los empeados
class Ciudades(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Ciudades"

#tabla para registrar empleados
class Empleados(models.Model):
    ci_numero=models.IntegerField()
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    telefono=models.IntegerField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Empleados"

#tabla para registrar clientes
class Clientes(models.Model):
    ci_numero=models.IntegerField()
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Clientes"

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
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Hoteles"
    
#tabla para registrar los tipos de habitaciones
class Tipo_Habitacion(models.Model):
    nombre=models.CharField(max_length=100)
    capacidad=models.IntegerField()
    costo=models.IntegerField()
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo_Habitaciones"

#tabla para registrar las habitaciones
class Habitacion(models.Model):
    numero=models.IntegerField()
    piso=models.IntegerField()
    id_tipo_habitacion=models.ForeignKey(Tipo_Habitacion, on_delete=models.CASCADE)
    id_hotel=models.ForeignKey(Hoteles, on_delete=models.CASCADE)
    def __str__(self):
        return "N°: "+str(self.numero)
    class Meta:
        verbose_name_plural = "Habitaciones"

#tabla para registrar las reservas
class Reservas(models.Model):
    id_cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha_entrada=models.DateTimeField()
    fecha_salida=models.DateTimeField()
    precio=models.IntegerField()
    numero_personas=models.IntegerField
    estado=models.CharField(max_length=50)
    id_habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Reservas"

#tabla para registrar las areas o departamentos dentro del hotel
class Areas(models.Model):
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Areas"

#tabla para registrar los cargos que se encuentran en cada area
class Cargo(models.Model):
    nombre=models.CharField(max_length=100)
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Cargos"

#tabla para registrar los puestos abiertos con las personas a cargo
class Puesto_Trabajo(models.Model):
    nombre=models.CharField(max_length=100)
    id_empleado=models.ForeignKey(Empleados, on_delete=models.CASCADE)
    id_cargo=models.ForeignKey(Cargo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Puesto_Trabajo"

#tabla para registrar mas de un huesped a una reserva
class Reserva_Huesped(models.Model):
    id_cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_reserva=models.ForeignKey(Reservas, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Reserva_Huespedes"