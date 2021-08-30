# Django
from django.db import models 

# Notification Abstract
from omnilatam.apps.notificacion.utils.models import NotificacionAbstract

class notificacion(NotificacionAbstract):

	class Meta(NotificacionAbstract.Meta):
		abstract = False