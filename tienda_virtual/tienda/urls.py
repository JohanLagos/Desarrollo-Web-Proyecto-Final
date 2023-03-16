from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('ropa', views.ropa, name='ropa'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

    path('actualizar_item', views.actualizar_item, name='actualizar_item'),
    path('proceso_pedido', views.proceso_pedido, name='proceso_pedido'),
]