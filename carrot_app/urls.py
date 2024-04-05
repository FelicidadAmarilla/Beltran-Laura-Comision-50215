from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('', home, name = 'home'),
    path('about_me', about_me, name = 'about_me'),

#________________________Tortas___________________________________________

    path('tortas/', tortas, name = 'tortas'),
    path('tortas_form/', TortasForm.as_view(), name='tortas_form'),
    path('tortas_create/', TortasCreate.as_view(), name='tortas_create'),
    path('tortas/update/<int:pk>/', TortasUpdate.as_view(), name= 'tortas_update'),
    path('tortas/delete/<int:pk>/', TortasDelete.as_view(), name='tortas_delete'),
    path('tortas_pedidos/', tortas_pedidos, name = 'tortas_pedidos'),
    path('search_pedidos_tor/', search_pedidos_tor, name='search_pedidos_tor'),

#________________________Catering___________________________________________

    path('catering/', catering, name = 'catering'),
    path('catering_form/', CateringForm.as_view(), name='catering_form'),
    path('catering_create/', CateringCreate.as_view(), name='catering_create'),
    path('catering/update/<int:pk>/', CateringUpdate.as_view(), name='catering_update'),
    path('catering/delete/<int:pk>/', CateringDelete.as_view(), name='catering_delete'),
    path('catering_pedidos/', catering_eventos, name = 'catering_eventos'),
    path('search_eventos/', search_eventos, name='search_eventos'),

#________________________Pastelería___________________________________________

    path('pasteleria/', pasteleria, name = 'pasteleria'),
    path('pasteleria_form/', PasteleriaForm.as_view(), name='pasteleria_form'),
    path('pasteleria_create/', PasteleriaCreate.as_view(), name='pasteleria_create'),
    path('pasteleria/update/<int:pk>/', PasteleriaUpdate.as_view(), name='pasteleria_update'),
    path('pasteleria/delete/<int:pk>/', PasteleriaDelete.as_view(), name='pasteleria_delete'),
    path('pasteleria_pedidos/', pasteleria_pedidos, name = 'pasteleria_pedidos'),
    path('search_pedidos_past/', search_pedidos_past, name='search_pedidos_past'),

#________________________Capacitaciones___________________________________________

    path('capacitaciones/', capacitaciones, name = 'capacitaciones'),
    path('capacitaciones_form/', CapacitacionesForm.as_view(), name='capacitaciones_form'),
    path('capacitaciones_create/', CapacitacionesCreate.as_view(), name='capacitaciones_create'),
    path('capacitaciones/update/<int:pk>/', CapacitacionesUpdate.as_view(), name='capacitaciones_update'),
    path('capacitaciones/delete/<int:pk>/', CapacitacionesDelete.as_view(), name='capacitaciones_delete'),
    path('capacitaciones_pedidos/', capacitaciones_curso, name = 'capacitaciones_curso'),
    path('search_curso/', search_pedidos_past, name='search_curso'),

#________________________Registro___________________________________________

    path('registro/', registro, name = 'registro'),

#________________________Login, Logout___________________________________________

    path('login/', login_request, name = 'login'),
    path('logout/', logout_request, name = 'logout'),

#________________________Edición perfil, Cambio de contraseña, Avatar_______________________

    path('perfil/', edit_profile, name='perfil'),
    path('<int:pk>/password/', CambiarContraseña.as_view(), name='cambiar_contrasena'),
    path('agregar_avatar/', agregar_avatar, name= 'agregar_avatar'),

]