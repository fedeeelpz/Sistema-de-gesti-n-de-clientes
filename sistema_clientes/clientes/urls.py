from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('deuda/editar/<int:deuda_id>/', views.editar_deuda, name='editar_deuda'),
    path('deuda/eliminar/<int:deuda_id>/', views.eliminar_deuda, name='eliminar_deuda'),
]