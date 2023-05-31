from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    path("registerCustomer/", views.registerCustomer, name="registerCustomer"),
    path("registerEmployes/", views.registerEmployes, name="registerEmployes"),
    path("registerHotel/", views.registerHotel, name="registerHotel")
]