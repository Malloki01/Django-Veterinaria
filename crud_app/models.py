from django.db import models

# Create your models here.

class Cita(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.CharField(max_length=200)

    class Meta:
        db_table = 'Cita'
