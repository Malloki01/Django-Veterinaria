from django.urls import path
from .views import mi_vista

urlpatterns = [
    path('', mi_vista, name='mi_vista'),
    # Otras rutas si es necesario
]