from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario= models.TextField(max_length=15)
    password_usuario = models.TextField(max_length=20)

class Estilo(models.Model):
    nombre_estilo = models.TextField(max_length=100)

class Pintura(models.Model):
    titulo_pintura = models.TextField(max_length=100)
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    precio_pintura = models.IntegerField(null=False)

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion_historial = models.TextField(max_length=200)
    tabla_afectada_historial = models.TextField(max_length=100)
    fecha_hora_historial = models.DateTimeField()   