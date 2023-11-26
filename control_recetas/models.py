from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    usuario = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class Recetas(models.Model):
    nombre=models.CharField(max_length=25)
    descripcion= models.CharField(max_length=1000)
    ingredientes = models.CharField(max_length=1000)
    autor = models.CharField(max_length=25)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre}"
