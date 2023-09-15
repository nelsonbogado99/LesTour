from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def signUp(request):
    if request.method == "GET":
        return render(request, "signUp.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                return HttpResponse("Registro completado satisfactoriamente")
            except:
                return render(
                    request,
                    "signUp.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )
        else:
            return render(
                request,
                "signUp.html",
                {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
            )
