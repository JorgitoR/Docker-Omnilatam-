

from django.contrib import admin

# Models 
from omnilatam.apps.notificacion.models import notificacion
from omnilatam.apps.notificacion.utils.admin import AbstractNotificacionAdmin

class NotificacionAdmin(AbstractNotificacionAdmin):
	raw_id_fields = ('receiver', )
	list_display = ('receiver', 'actor', 'verb', 'level', 'read')
	list_filter = ('level', 'read', 'timestamp')

admin.site.register(notificacion, NotificacionAdmin)