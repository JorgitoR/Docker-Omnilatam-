from django.urls import path, include


from omnilatam.apps.order.api.views import ProductViewSet, ProductListAPIView

# Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='users')


urlpatterns = [
	
	path('', include(router.urls)),
	path('product/list', ProductListAPIView.as_view())

]