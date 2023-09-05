from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Traduccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    texto_ingles = models.TextField()
    texto_espanol = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto_ingles


class HistorialTraduccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto_original = models.TextField(default="")
    texto_traducido = models.TextField(null=True, default=None)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.texto_original


class Busqueda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    consulta = models.CharField(max_length=255)

    def __str__(self):
        return self.consulta
