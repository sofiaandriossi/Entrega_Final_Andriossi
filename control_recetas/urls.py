from django.urls import path
from control_recetas.views import listar_usuarios, listar_recetas, crear_receta, crear_usuario, buscar_usuario, buscar_receta, eliminar_receta

urlpatterns = [
    path("usuario/", listar_usuarios, name="lista_usuarios" ),
    path("crear-receta/", crear_receta, name="crear_receta"),
    path("recetas/", listar_recetas, name="lista_recetas"),
    path("crear-usuario/", crear_usuario, name="crear_usuario"),
    path("buscar-usuario/", buscar_usuario, name="buscar_usuario"),
    path("buscar-receta/", buscar_receta, name="buscar_receta"),
    path("eliminar-receta/<int:id>/", eliminar_receta, name="eliminar_receta")

    ]