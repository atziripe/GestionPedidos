from django.shortcuts import render, redirect
from .carrito import Carrito
from tienda.models import Producto

def add_product(request, id_prod):
    carrito =  Carrito(request)
    producto = Producto.objects.get(id=id_prod)
    carrito.agregar(prod=producto)
    return redirect("tienda")

def delete_product(request, id_prod):
    carrito =  Carrito(request)
    producto = Producto.objects.get(id=id_prod)
    carrito.eliminar_producto(prod=producto)
    return redirect("tienda")

def substract_product(request, id_prod):
    carrito =  Carrito(request)
    producto = Producto.objects.get(id=id_prod)
    carrito.restar_producto(prod=producto)
    return redirect("tienda")

def clean_carrito(request, id_prod):
    carrito =  Carrito(request)
    carrito.limpiar_carrito()
    return redirect("tienda")