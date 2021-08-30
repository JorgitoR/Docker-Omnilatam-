"""Order models."""

# Django
from django.db import models

# Utilities
from omnilatam.apps.utils.models import BaseModel


# ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 

# Models
from omnilatam.apps.user.models import User


PURCHASE_STATUS = (
    ('sent', 'Sent'),
    ('received', 'Received'),
)

class OrderProduct(BaseModel):
	"""Order product models.
	"""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content_type = models.ForeignKey(
		ContentType,
		verbose_name="models product",
		on_delete=models.CASCADE
	)
	object_id = models.PositiveIntegerField(
		"id of the product"
	)
	content_object = GenericForeignKey("content_type", "object_id")

	purchased = models.BooleanField(default=False)
	amount = models.IntegerField(default=1)

	def __str__(self):
		return self.user.username


class Order(BaseModel):
	"""Order Models.

	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
	product = models.ManyToManyField(OrderProduct, through='ProductsOrdered')
	purchased = models.BooleanField(default=False)
	status = models.CharField(max_length=100, choices=PURCHASE_STATUS)


	def __str__(self):
		"""Return user"""
		return self.user.username


class ProductsOrdered(models.Model):
	product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)


	def __str__(self):
		return "User: {} ordered the next product: {}".format(self.product.content_object.user.username, self.content_object.title)