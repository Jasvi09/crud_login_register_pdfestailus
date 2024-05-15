from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cursos (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    duracion = models.CharField(max_length=5)
    link = models.TextField()
    creador = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " | " + self.descripcion + " | " + self.duracion + " | " + self.creador
