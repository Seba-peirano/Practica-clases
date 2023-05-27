from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    nombre=models.CharField(max_length=30)
    comision=models.IntegerField()
    creador=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self) :
        return f"{self.nombre}| {self.comision}"
class Socio(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()
    creador=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Visitante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()

class Entregable(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField()
    esta_aprobado=models.BooleanField(default=False)
    creador=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    