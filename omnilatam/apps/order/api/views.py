"""User Views."""

# Django REST Fremework
from rest_framework import mixins, status, viewsets, generics
from rest_framework.decorators import action 
from rest_framework.response import Response

# Paginatin
from omnilatam.apps.order.api.pagination import StandardResultsPagination

# Permissions
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated
)

# Serializers
#from omnilatam.apps.order.api.serializers.order import ProfileModelSerializers
from omnilatam.apps.order.api.serializers.product import ProductModelSerializer


# Models
from omnilatam.apps.order.models.product import Product


class ProductViewSet(mixins.RetrieveModelMixin,
				  mixins.UpdateModelMixin,
				  mixins.CreateModelMixin,
				  viewsets.GenericViewSet):
	"""User view set

	Handle sign up, login and account verification
	"""

	queryset = Product.objects.all()
	serializer_class = ProductModelSerializer
	lookup_field='slug'


	@action(detail=False, methods=['post'])
	def created(self, request):
		"""User sign in."""
		serializer = UserModelSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		product = serializer.save()
		data = {
			'user':UserModelSerializer,
			
		}

		return Response(data, status=status.HTTP_201_CREATED)


class ProductListAPIView(generics.ListAPIView):
	"""retrieve the list of the all products."""

	queryset = Product.objects.all()
	serializer_class=ProductModelSerializer
	pagination_class = StandardResultsPagination

