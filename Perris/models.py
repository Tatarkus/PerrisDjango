from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
	user=models.OneToOneField(User, on_delete = models.CASCADE)
	run = nombre=models.CharField(max_length=30)
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	telefono=models.IntegerField()

	def __str__(self):
		datos = {
			'run':self.user.run,
			'nombre':self.nombre,
			'apellido':self.apellido,
			'email':self.email,
			'telefono':self.telefono
		}
		return datos

class Mascota(models.Model):
	codigo=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=30)
	color=models.CharField(max_length=20)

class Adopcion(models.Model):
	run=models.ForeignKey(Cliente,on_delete=models.CASCADE)
	codigo=models.ForeignKey(Mascota,on_delete=models.CASCADE)