from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),

#________________________Tortas___________________________________________

    path('tortas/', tortas, name = 'tortas'),
    path('tortas_form/', TortasForm.as_view(), name='tortas_form'),
    path('tortas_create/', TortasCreate.as_view(), name='tortas_create'),
    path('tortas/update/<int:pk>/', TortasUpdate.as_view(), name= 'tortas_update'),
    path('tortas/delete/<int:pk>/', TortasDelete.as_view(), name='tortas_delete'),
    path('tortas_pedidos/', tortas_pedidos, name = 'tortas_pedidos'),

#________________________Catering___________________________________________

    path('catering/', catering, name = 'catering'),
    path('catering_form/', CateringForm.as_view(), name='catering_form'),
    path('catering_create/', CateringCreate.as_view(), name='catering_create'),
    path('catering/update/<int:pk>/', CateringUpdate.as_view(), name='catering_update'),
    path('catering/delete/<int:pk>/', CateringDelete.as_view(), name='catering_delete'),
    path('catering_pedidos/', catering_eventos, name = 'catering_eventos'),

#________________________Pastelería___________________________________________

    path('pasteleria/', pasteleria, name = 'pasteleria'),
    path('pasteleria_form/', PasteleriaForm.as_view(), name='pasteleria_form'),
    path('pasteleria_create/', PasteleriaCreate.as_view(), name='pasteleria_create'),
    path('pasteleria/update/<int:pk>/', PasteleriaUpdate.as_view(), name='pasteleria_update'),
    path('pasteleria/delete/<int:pk>/', PasteleriaDelete.as_view(), name='pasteleria_delete'),
    path('pasteleria_pedidos/', pasteleria_pedidos, name = 'pasteleria_pedidos'),

#________________________Capacitaciones___________________________________________

    path('capacitaciones/', capacitaciones, name = 'capacitaciones'),
    path('capacitaciones_form/', CapacitacionesForm.as_view(), name='capacitaciones_form'),
    path('capacitaciones_create/', CapacitacionesCreate.as_view(), name='capacitaciones_create'),
    path('capacitaciones/update/<int:pk>/', CapacitacionesUpdate.as_view(), name='capacitaciones_update'),
    path('capacitaciones/delete/<int:pk>/', CapacitacionesDelete.as_view(), name='capacitaciones_delete'),
    path('capacitaciones_pedidos/', capacitaciones_curso, name = 'capacitaciones_curso'),


]