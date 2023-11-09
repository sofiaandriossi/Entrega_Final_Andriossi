from django.contrib import admin

from control_recetas.models import Recetas, Cocinero, Usuario

admin.site.register(Recetas)
admin.site.register(Cocinero)
admin.site.register(Usuario)
