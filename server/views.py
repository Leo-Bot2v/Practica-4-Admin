from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def espacios(request):
    return render(request, "espacios_publicitarios.html")

def compras(request):
    return render(request, "compras_ventas.html")

def contacto(request):
    return render(request, "contactanos.html")

def mensaje(request):
    nombre = request.POST.get("nombre", "")
    return render(request, "mensaje.html", {"nombre": nombre})