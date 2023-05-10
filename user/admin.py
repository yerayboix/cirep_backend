from django.contrib import admin

from report.models import Incidencia, TipoIncidencia, IncidenciaPorNotificar
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email")


admin.site.register(models.User, UserAdmin)
admin.site.register(Incidencia)
admin.site.register(TipoIncidencia)
admin.site.register(IncidenciaPorNotificar)
