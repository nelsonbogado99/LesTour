from django.shortcuts import render
from . import forms

#pagina principal o Home
def index(request):
    return render(request, "pages/index.html")

#pagina de registro de clientes
def registerCustomer(request):
    return render(request, "pages/registerCustomer.html", {"form":forms.RegisterCustomerForm()})

def  registerEmployes(request):
    return render(request,"pages/registerEmployes.html",{"form":forms.RegisterEmployesForm()})