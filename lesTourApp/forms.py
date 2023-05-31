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