from django.shortcuts import render
from . import forms

#pagina principal o Home
def index(request):
    return render(request, "pages/index.html")

#pagina de registro de clientes
def registerCustomer(request):
    return render(request, "pages/registerCustomer.html", {"form":forms.RegisterCustomerForm()})

#pagina de registro de nuevos trabajadores
def  registerEmployes(request):
    return render(request,"pages/registerEmployes.html",{"form":forms.RegisterEmployesForm()})

#pagina de registro de nuevos hoteles
def  registerHotel(request):
    return render(request,"pages/registerHotel.html",{"form":forms.RegisterHotelForm()})