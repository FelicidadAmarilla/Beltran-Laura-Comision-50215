from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = 'home'),

#________________________Tortas___________________________________________
    path('tortas/', tortas, name = 'tortas'),
    path('tortas_form/', TortasForm.as_view(), name='tortas_form'),
   
    path('tortas_update/<int:pk>/', TortaUpdate.as_view(), name='tortas_update'),
    path('tortas/delete/<int:pk>/', TortasDelete.as_view(), name='tortas_delete'),
    path('tortas_pedidos/', tortas_pedidos, name = 'tortas_pedidos'),
    path('tortas_pedidos_search/', search_pedidos, name = 'search_pedidos'),

#________________________Catering___________________________________________
    path('catering/', catering, name = 'catering'),
    path('pasteleria/', pasteleria, name = 'pasteleria'),
    path('capacitaciones/', capacitaciones, name = 'capacitaciones'),




#________________________Pastelería___________________________________________
    path('catering_form/', CateringForm.as_view(), name='catering_form'),
    path('pasteleria_form/', PasteleriaForm.as_view(), name='pasteleria_form'),
    path('capacitaciones_form/', CapacitacionesForm.as_view(), name='capacitaciones_form'),


#________________________Capacitaciones___________________________________________


]