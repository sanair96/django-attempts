from django.db import models

# Create your models here.

class form(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	"""docstring for form"""
	def __str__(self):
		return self.name

