from django.db import models

class Usuario(models.Model):
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    usuario = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cocinero(models.Model):
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    titulacion= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Recetas(models.Model):
    nombre=models.CharField(max_length=25)
    descripcion= models.CharField(max_length=250)
    ingredientes = models.CharField(max_length=250)
    autor = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nombre}"
