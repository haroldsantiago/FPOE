from django.db import models

class Computador(models.Model):
	marca 				= models.TextField()
	procesador			= models.TextField()
	memoriaRam			= models.TextField()
	almacenamiento		= models.TextField()
	def __str__(self):
		return self.marca