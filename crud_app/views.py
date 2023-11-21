# Create your views here.
# views.py

from django.shortcuts import render, redirect
from .models import Cita

def mi_vista(request):
    return render(request, 'index.html')

def registrarCita(request):
    nombre = request.POST["nombre"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
    mensaje = request.POST["mensaje"]
    
    cita = Cita(nombre=nombre, telefono=telefono, correo=correo, mensaje=mensaje)
    cita.save()
    return redirect("/crud_app/")
    