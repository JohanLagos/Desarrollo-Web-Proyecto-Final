from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre
    
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_pedido = models.DateField(auto_now_add=True)
    completo = models.BooleanField(default=False, null=True, blank=False)
    id_transaccion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_total_carrito(self):
        items_pedido = self.itemspedido_set.all()
        total = sum([item.get_total for item in items_pedido])
        return total
    
    @property
    def get_items_carrito(self):
        items_pedido = self.itemspedido_set.all()
        total = sum([item.cantidad for item in items_pedido])
        return total


class ItemsPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total


class DireccionCompra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    zipcodigo = models.CharField(max_length=200)
    fecha_agregado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.direccion
