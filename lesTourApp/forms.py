from django import forms

class RegisterCustomerForm(forms.Form):
    ci_numero=forms.IntegerField(label="N° C.I.:")
    nombre=forms.CharField(label="Nombre:")
    email=forms.CharField(label="Correo:")
    direccion=forms.CharField(label="Direccion:")
    telefono=forms.IntegerField(label="Telefono:")

class RegisterEmployesForm(forms.Form):
    ci_numero=forms.IntegerField(label="N° C.I.:")
    nombre=forms.CharField(label="Nombre:")
    email=forms.CharField(label="Correo:")
    direccion=forms.CharField(label="Direccion:")
    telefono=forms.IntegerField(label="Telefono:")

class RegisterHotelForm(forms.Form):
    nombre=forms.CharField(label="Nombre:")
    ciudad=forms.CharField(label="Ciudad:")
    barrio=forms.CharField(label="Barrio:")
    direccion=forms.CharField(label="Direccion:")
    telefono=forms.IntegerField(label="Telefono:")
    email=forms.CharField(label="Correo:")
    pisos=forms.IntegerField(label="N° Pisos:")
    habitaciones=forms.IntegerField(label="N° Habitaciones:")