from django.db import models

# Create your models here.
class Stock(models.Model):
	date = models.DateTimeField()
	openPrice = models.FloatField()
	low = models.FloatField()
	high = models.FloatField()
	closePrice = models.FloatField()
	volume = models.FloatField()

	def __str__(self):
		return self.date