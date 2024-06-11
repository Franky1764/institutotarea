from django.shortcuts import render

# Create your views here.

# Declaración de un objeto.
class persona:
        def __init__(self, nombre, edad):
            self.nombre=nombre
            self.edad=edad
            super().__init__()


def index (request):
    
    hijo = persona ("Vicente Saavedra", "6")
    lista = ["Lazaña", "Chariquicán", "Porotos Granados"]
    
    context={"hijo": hijo, "nombre":"César Saavedra", "comidas":lista}
    
    return render(request, 'alumnos/index.html', context)