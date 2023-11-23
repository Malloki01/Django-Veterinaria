# Create your tests here.
from django.test import TestCase
from faker import Faker
from crud_app.models import Cita

class TusPruebas(TestCase):
    def setUp(self):
        # Configurar Faker con el proveedor de es_MX
        self.fake = Faker('es_MX')
        
    def test_creacion_de_datos_falsos(self):
        # Ejemplo de creación de datos falsos
        nombre_falso = self.fake.name()
        telefono_falso = self.fake.phone_number()
        correo_falso = self.fake.email()
        mensaje_falso = self.fake.paragraph()

        # Usar los datos falsos en la creación de un objeto en tu modelo
        cita = Cita.objects.create(
            nombre=nombre_falso,
            telefono=telefono_falso,
            correo=correo_falso,
            mensaje=mensaje_falso,
        )

        # Verificar que el objeto se ha creado correctamente
        self.assertEqual(cita.nombre, nombre_falso, f'El nombre debería ser {nombre_falso}')
        self.assertEqual(cita.telefono, telefono_falso, f'El telefono debería ser {telefono_falso}')
        self.assertEqual(cita.correo, correo_falso, f'El correo debería ser {correo_falso}')
        self.assertEqual(cita.mensaje, mensaje_falso, f'El mensaje debería ser {mensaje_falso}')



