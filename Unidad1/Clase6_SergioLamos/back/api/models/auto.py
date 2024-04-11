from django.db import models

class Auto(models.Model):
	marca 		= models.CharField(max_length=50)
	velocidad 	= models.FloatField()
	placa 		= models.TextField()
	color 		= models.TextField()

	def __str__(self):
		return self.marca