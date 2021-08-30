"""Product models."""

# Django
from django.db import models

# Utilities
from omnilatam.apps.utils.models import BaseModel
from django.utils.html import mark_safe, escape
from django.utils.text import slugify

# Models
from omnilatam.apps.user.models import User

class Category(BaseModel):
	"""Category models.
	we'll category the products eg. products for house,
	for health care..
	
	"""
	name = models.CharField(
		max_length=20
	)
	color = models.CharField(
		max_length=7, default='#06C503'
	)


	def __str__(self):
		return self.name

	def get_badge(self):
		name = escape(self.name)
		color = escape(self.color)
		html = '<button style="background:%s"> %s </>' %(self.color, self.name)
		return mark_safe(html)

class Product(BaseModel):
	"""Produc models.
		Handle the products for the e-commerce
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
	title = models.CharField(max_length=100)
	description = models.TextField()

	stock = models.IntegerField()
	price = models.FloatField()

	slug = models.SlugField(blank=True, null=True, unique=True)

	parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
	relateds = models.ManyToManyField('self', blank=True, related_name='relacion', through='ProductRelated',  symmetrical=False)


	def __str__(self):
		"""Return title."""
		return self.title


class ProductRelated(BaseModel):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	related = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="item_related")