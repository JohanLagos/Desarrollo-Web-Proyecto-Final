from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('inicio', views.inicio, name='inicio'),
    path('ropa', views.ropa, name='ropa'),
    path('zapatos', views.store, name='zapatos'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

    path('actualizar_item', views.actualizar_item, name='actualizar_item'),
    path('proceso_pedido', views.proceso_pedido, name='proceso_pedido'),
]