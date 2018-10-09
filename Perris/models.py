from django.db import models

# Create your models here.
class Cliente(models.Model):
    run=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.IntegerField(max_length=9)

class Mascota(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=20)

class ClienteMascota