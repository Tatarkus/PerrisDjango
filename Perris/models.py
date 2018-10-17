from django.db import models
from django.contrib.auth.models import User

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

class Adopcion(models.Model):
	run=models.ForeignKey(Cliente,on_delete=models.CASCADE)
	codigo=models.ForeignKey(Mascota,on_delete=models.CASCADE)