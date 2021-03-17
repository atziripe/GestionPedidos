from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "proyectoWebApp/Index.html")

def tienda(request):
    return render(request, "proyectoWebApp/Tienda.html")

