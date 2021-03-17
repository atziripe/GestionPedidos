from django.shortcuts import render
from servicios.models import Servicio

def servicios(request):
    services = Servicio.objects.all() #importar todos los servicios que estan en el modelo Servicio
    return render(request, "servicios/Servicios.html",{"servicios":services})