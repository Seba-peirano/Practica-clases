from django.db import models

class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    comision=models.IntegerField()
    def __str__(self) :
        return f"{self.nombre}| {self.comision}"
class Socio(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Visitante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()

class Post(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField()
    esta_aprobado=models.BooleanField(default=False)
    