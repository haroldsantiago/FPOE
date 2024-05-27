from django.db import models

class Servicio(models.Model):
	nombre 		= models.TextField()
	cedula 	    = models.TextField()
	descripcion = models.TextField()
	valor 		= models.TextField()

	def __str__(self):
		return self.nombre 