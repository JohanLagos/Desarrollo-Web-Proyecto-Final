from django.shortcuts import render

from django.http import JsonResponse

import json
import datetime

from .models import *
from .utils import cookieCart, cartData, pedidoInvitado

# Create your views here.
def store(request):
    data = cartData(request)
    
    item_carrito = data['carritoItems']

    productos = Producto.objects.all()
    context = {'productos' : productos, 'item_carrito': item_carrito}
    return render(request, 'store/store.html', context)

def ropa(request):
    data = cartData(request)
    
    item_carrito = data['carritoItems']

    ropa = Ropa.objects.all()
    context = {'ropas' : ropa, 'item_carrito': item_carrito}
    return render(request, 'store/ropa.html', context)

def cart(request):

    data = cartData(request)
    
    item_carrito = data['carritoItems']
    pedido = data['pedido']
    items = data['items']

    context = {'items': items, 'pedido': pedido, 'item_carrito': item_carrito}

    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)

    item_carrito = data['carritoItems']
    pedido = data['pedido']
    items = data['items']

    context = {'items': items, 'pedido': pedido, 'item_carrito': item_carrito}
    
    return render(request, 'store/checkout.html', context)

def actualizar_item(request):
    data = json.loads(request.body)
    id_producto = data['id_producto']
    accion = data['accion']

    print('Accion:', accion)
    print('ID Producto:', id_producto)

    cliente = request.user.cliente
    producto = Producto.objects.get(id=id_producto)    

    pedido, creado = Pedido.objects.get_or_create(cliente = cliente, completo = False)
    itemPedido, creado = ItemsPedido.objects.get_or_create(pedido= pedido, producto = producto)

    if accion == 'add':
        itemPedido.cantidad = (itemPedido.cantidad + 1)
    elif accion == 'remove':
        itemPedido.cantidad = (itemPedido.cantidad - 1)
    
    itemPedido.save()

    if itemPedido.cantidad <= 0:
        itemPedido.delete()

    return JsonResponse('Item fue agregado', safe=False)

def proceso_pedido(request):
    print("Datos:", request.body)
    transaccion_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body) 

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, creado = Pedido.objects.get_or_create(cliente = cliente, completo = False)

    else:
        cliente, pedido = pedidoInvitado(request, data)

    total = float(data['usuario']['total'])
    pedido.id_transaccion = transaccion_id

    if total == pedido.get_total_carrito:
        pedido.completo = True
    pedido.save()

    if pedido.completo == True:
        DireccionCompra.objects.create(
            cliente = cliente,
            pedido = pedido,
            direccion = data['envio']['direccion'],
            ciudad= data['envio']['ciudad'],
            estado= data['envio']['estado'],
            zipcodigo= data['envio']['zipcode'],
        )

    return JsonResponse('Pago Completado', safe=False)

