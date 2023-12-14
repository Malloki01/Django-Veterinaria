from django.urls import path
from . import views
from .views import  mi_vista ,listar_citas, detalle_cita, editar_cita, eliminar_cita
from .views import signin
from .views import generar_factura_pdf


urlpatterns = [
    path('', mi_vista, name='mi_vista'),
    path('client', views.client, name='client'),
    path('contact', views.contact, name='contact'),
    path('index', views.mi_vista, name='index'),
    path('login', views.login, name='login'),

    
    #Funciones CRUD
    path('registrarCita', views.registrarCita, name='registrarCita'),
    
    path('listar_citas', views.listar_citas, name='listar_citas'),
    path('app_crud/<int:id>/', detalle_cita, name='detalle_cita'),
    #Revisar esta parte
    path('cita/editar/<int:id>/', editar_cita, name='editar_cita'),
    path('cita/eliminar/<int:id>/', eliminar_cita, name='eliminar_cita'),

    #Login
    path('signin', signin, name='signin'),

    # Generar Factura
    path('factura/<int:cita_id>/pdf/', generar_factura_pdf, name='generar_factura_pdf'),

]