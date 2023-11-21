from django.urls import path
from . import views
from .views import mi_vista

urlpatterns = [
    path('', mi_vista, name='mi_vista'),
    path('registrarCita', views.registrarCita, name='registrarCita')
]