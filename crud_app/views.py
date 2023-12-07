# Create your views here.
# views.py

from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from .forms import CitaForm  # Necesitarás crear un formulario (forms.py) para el modelo Cita

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

#Vistas de las páginas
def mi_vista(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def client(request):
    return render(request, 'client.html')

def login(request):
    return render(request, 'login.html')

#Funciones CRUD
def registrarCita(request):
    nombre = request.POST["nombre"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
    mensaje = request.POST["mensaje"]
    
    cita = Cita(nombre=nombre, telefono=telefono, correo=correo, mensaje=mensaje)
    cita.save()
    return redirect("/crud_app/")

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    return redirect('listar_citas')

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'listar_citas.html', {'citas': citas})

def detalle_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    return render(request, 'detalle_cita.html', {'cita': cita})

def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'cita/editar_cita.html', {'form': form})

#Login

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request)  
            return redirect('listar_citas')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')