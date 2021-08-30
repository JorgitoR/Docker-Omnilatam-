"""Product serializers."""

# Django REST Framework
from rest_framework import serializers

# Models 
from omnilatam.apps.order.models.product import Product


class ProductModelSerializer(serializers.ModelSerializer):

	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:

		model = Product
		fields = ('user', 'category', 'title', 'description', 'stock', 'price')