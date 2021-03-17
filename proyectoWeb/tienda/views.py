from django.shortcuts import render, HttpResponse

def tienda(request):
    return render(request, "tienda/Tienda.html")