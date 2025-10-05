from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("espacios/", views.espacios, name="espacios"),
    path("compras/", views.compras, name="compras"),
    path("contacto/", views.contacto, name="contacto"),
    path("mensaje/", views.mensaje, name="enviar_mensaje"),
]