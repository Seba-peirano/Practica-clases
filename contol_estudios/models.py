from django.db import models

class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    comision=models.IntegerField()
    def __str__(self) :
        return f"{self.nombre}| {self.comision}"
class Estudiante(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()
    telefono=models.CharField(max_length=20, blank=True)
    dni=models.CharField(max_length=32)
    fecha_nacimiento=models.DateField()
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=256)
    apellido=models.CharField(max_length=256)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    dni=models.CharField(max_length=32)
    fecha_nacimiento=models.DateField()
    bio=models.TextField()
    profesion=models.CharField(max_length=256)

class Entregable(models.Model):
    nombre=models.CharField(max_length=256)
    fecha_entrega=models.DateTimeField()
    esta_aprobado=models.BooleanField(default=False)
    