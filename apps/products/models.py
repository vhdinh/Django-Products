from __future__ import unicode_literals

from django.db import models

class ProductManager(models.Manager):
	def get(self):
		return self.all()

	def create(self, name, description, price):
		errors = {}
		if len(name) < 1 or len(description) < 1 or len(price) < 1:
			errors['form'] = "All fields need to be filled out" 
		if errors:
			return (False, errors)
		p1 = self.save(name=name, description=description, price=price)
		return (True, p1)
		
	def getProd(self, product_id):
		return self.filter(id=product_id)[0]

	def updateProd(self, product_id, name, description, price):
		errors = {}
		if len(name) < 1 or len(description) < 1 or len(price) < 1:
			errors['form'] = "All fields need to be filled out" 
		if errors:
			return (False, errors)
		return (True, self.filter(id=product_id).update(name=name, description=description,price=price))
		


	def remove(self, product_id):
		return self.filter(id=product_id).delete()


# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True)
	productManager = ProductManager()
	objects = models.Manager()
	def __str__(self):
		return self.name
	class Meta():
		db_table = "products"