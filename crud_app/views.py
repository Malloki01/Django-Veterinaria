# Create your views here.
# views.py

from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect, get_object_or_404

from django_crud.settings import PDFKIT_COMMAND
from .models import Cita
from .forms import CitaForm  # Necesitarás crear un formulario (forms.py) para el modelo Cita

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse 
from reportlab.pdfgen import canvas
import datetime

from django.views.generic import View
from django.template.loader import render_to_string
from pdfkit import from_string


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

#Generar PDF
from reportlab.platypus import Table

def generar_factura_pdf(request, cita_id):
    cita = Cita.objects.get(id=cita_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{cita.nombre}.pdf"'

    p = canvas.Canvas(response)
    
    # Agrega el encabezado de la factura
    p.setFont("Helvetica", 14)
    p.drawString(100, 75, "Empresa XYZ")
    p.drawString(100, 60, "Factura")
    p.drawString(100, 45, f'Fecha: {datetime.date.today()}')

    # Agrega una línea en blanco
    p.line(100, 30, 500, 30)

    # Agrega los datos del cliente
    p.setFont("Helvetica", 12)
    p.drawString(250, 75, f'Cliente: {cita.nombre}')
    p.drawString(250, 60, f'Empresa: {"Veterinarias Lupita"}')
    p.drawString(250, 45, f'Dirección: {"Breña, Lima"}')

    # Agrega el total de la factura
    p.setFont("Helvetica", 12)

    # Agrega los detalles de la factura

    # Crea una tabla con las columnas adecuadas
    table_data = [("Descripción", "Total")]

    # Agrega los datos de la tabla
    table_data.extend([(cita.mensaje, "20")])

    # Crea la tabla
    table = Table(table_data)

 # Centra la tabla horizontalmente
    table.hAlign = 'CENTER'

    # Centra la tabla verticalmente
    table.vAlign = 'MIDDLE'

    # Establece el estilo de la tabla
    table.setStyle([
        ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        # Aumenta el tamaño de la letra del encabezado a 20 puntos
        ('FONTSIZE', (0, 0), (-1, 0), 15),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('BACKGROUND', (0, 1), (-1, -1), 'LightBlue'),
        ('TEXTCOLOR', (0, 1), (-1, -1), 'black'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        # Aumenta el tamaño de la letra del cuerpo de la tabla a 25 puntos
        ('FONTSIZE', (0, 1), (-1, -1), 15),
        # Ajusta el alineamiento del encabezado a la izquierda
        ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
    ])

    # Agrega la tabla a la factura
    table.wrapOn(p, 400, 200)
    table.drawOn(p, 100, 200)

    p.save()

    return response


