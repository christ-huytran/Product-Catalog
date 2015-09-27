from django.db import models

# Create your models here.
class Manufacturer(models.Model):
	manufacturer_name = models.CharField(max_length=100)
	class Meta:
		db_table = 'manufacturers'

class Product(models.Model):
	product_name = models.CharField(max_length=150)
	price = models.FloatField()
	manufacturer = models.ForeignKey(Manufacturer)
	date_added = models.DateField(auto_now_add=True)
	class Meta:
		db_table = 'products'