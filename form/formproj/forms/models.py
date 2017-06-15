from django.db import models

# Create your models here.

class form(models.Models):
	name = models.CharField(max_Length = 15)

	"""docstring for form"""
	def __str__(self):
		return self.name