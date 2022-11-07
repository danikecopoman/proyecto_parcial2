from django.contrib import admin

from apps.vianda.models import TipoPlato, Vianda

# Register your models here.
admin.site.register(TipoPlato),
admin.site.register(Vianda)
