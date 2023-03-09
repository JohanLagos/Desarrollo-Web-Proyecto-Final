import json
from .models import *

def cookieCart(request):
    try:
        carrito = json.loads(request.COOKIES['cart'])
    except: 
        carrito = {}

    print('Carito:', carrito)
    items = []
    pedido = {'get_total_carrito': 0,
            'get_items_carrito': 0}
    item_carrito = pedido['get_items_carrito']

    for i in carrito:
        try:
            item_carrito += carrito[i]['cantidad']

            producto = Producto.objects.get(id=i)
            total = (producto.precio * carrito[i]['cantidad'])

            pedido['get_total_carrito'] += total
            pedido['get_items_carrito'] += carrito[i]['cantidad']

            item = {
                'producto':{
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio' : producto.precio,
                    'imagenURL': producto.imagenURL,
                },
                'cantidad': carrito[i]['cantidad'],
                'get_total': total
            }

            items.append(item)
        except:
            pass

    return {'carritoItems': item_carrito, 'pedido': pedido, 'items': items}

def cartData(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, creado = Pedido.objects.get_or_create(cliente = cliente, completo = False)
        items = pedido.itemspedido_set.all()
        item_carrito = pedido.get_items_carrito
    else:
        cookieData = cookieCart(request)
        item_carrito = cookieData['carritoItems']
        pedido = cookieData['pedido']
        items = cookieData['items']
        
    return {'carritoItems': item_carrito, 'pedido': pedido, 'items': items}

def pedidoInvitado(request, data):
    print("Usuario no se a logueado")
        
    print("COOKIES:", request.COOKIES)

    nombre = data['usuario']['nombre']
    email = data['usuario']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    cliente, creado = Cliente.objects.get_or_create(
        email=email,
    )
    cliente.nombre = nombre # lo creamos afuero por si el cliente se registra con el mismo correo y cambia el nombre
    cliente.save()

    pedido = Pedido.objects.create(
        cliente = cliente,
        completo = False
    )

    for item in items:
        producto = Producto.objects.get(id=item['producto']['id'])
        itemPedido = ItemsPedido.objects.create(
            producto = producto,
            pedido = pedido,
            cantidad = item['cantidad']
        )

    return cliente, pedido