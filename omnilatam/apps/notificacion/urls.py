from django.urls import path

from omnilatam.apps.notificacion.views import Notificaciones

urlpatterns = [
	
	path('notify/', Notificaciones.as_view(), name='notificaciones')
]