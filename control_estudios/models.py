from django.db import models


class Curso(models.Model):
    nombre= models.CharField(max_length= 64)
    comision = models.IntegerField()

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email= models.EmailField(blank=True)
    telefono= models.CharField(max_length=20, blank=True)
    dni= models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email= models.EmailField(blank=True)
    profesion= models.CharField(max_length=128)
    dni= models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

class Entregable(models.Model):
    nombre= models.Charfield(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False)
