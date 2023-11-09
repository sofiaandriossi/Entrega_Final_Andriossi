from django.db import models

class Usuario(models.Model):
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    email= models.EmailField(blank=True)
    usuario = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cocinero(models.Model):
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    email= models.EmailField(blank=True)
    dni= models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    titulacion= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Recetas(models.Model):
    receta = models.CharField(max_length=25)
    descripcion= models.CharField(max_length=250)
    ingredientes = models.CharField(max_length=250)
    autor = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.nombre}"


class Reseña(models.Model):
    reseña = models.CharField(max_length=256)
    me_gusta = models.BooleanField(default=False)
    autor= models.CharField(max_length=25)
