from django.urls import path
from control_recetas.views import listar_usuarios, listar_recetas, crear_receta

urlpatterns = [
    path("usuario/", listar_usuarios, name="lista_usuarios" ),
    path("crear-receta/", crear_receta, name="crear_receta"),
    path("recetas/", listar_recetas, name="lista_recetas")
    ]