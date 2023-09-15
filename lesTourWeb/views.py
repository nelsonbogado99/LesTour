from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")

def signUp(request):
    if request.method == "GET":
        return render(request, "signUp.html",{
        "form":UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            #Register user
            try:
                user= User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                return HttpResponse("Registro completado satisfactoriamente")
            except:
                return HttpResponse("Nombre de usuario ya existe")
        else:
            return HttpResponse("Las Contraseñas no coinciden")