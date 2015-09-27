from django.db import models

# Create your models here.
class Manufacturer(models.Model):
	def __unicode__(self):
		return self.manufacturer_name
	manufacturer_name = models.CharField(max_length=100)
	class Meta:
		db_table = 'manufacturers'

class Product(models.Model):
	def __unicode__(self):
		return self.product_name
	product_name = models.CharField(max_length=200)
	price = models.FloatField()
	manufacturer = models.ForeignKey(Manufacturer)
	date_added = models.DateField(auto_now_add=True)
	class Meta:
		db_table = 'products'