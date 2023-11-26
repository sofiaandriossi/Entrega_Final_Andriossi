from django.urls import path
from control_recetas.views import listar_usuarios, crear_usuario, buscar_usuario, buscar_receta, editar_usuario, eliminar_usuario, RecetaListView, RecetaDetailView, RecetaCreateView, RecetaUpdateView, RecetaDeleteView 

urlpatterns = [
    path("usuario/", listar_usuarios, name="lista_usuarios" ),
    path("crear-usuario/", crear_usuario, name="crear_usuario"),
    path("buscar-usuario/", buscar_usuario, name="buscar_usuario"),
    path("buscar-receta/", buscar_receta, name="buscar_receta"),
    path("editar-usuario/<int:id>/", editar_usuario, name="editar_usuario"),
    path("eliminar-usuario/<int:id>/", eliminar_usuario, name="eliminar_usuario"),
    path("recetas/", RecetaListView.as_view(), name="lista_recetas"),
    path("recetas/<int:pk>/", RecetaDetailView.as_view(), name="ver_receta"),
    path("crear-receta/", RecetaCreateView.as_view(), name="crear_receta"),
    path("editar-receta/<int:pk>/", RecetaUpdateView.as_view(), name="editar_receta"),
    path("eliminar-receta/<int:pk>/", RecetaDeleteView.as_view(), name="eliminar_receta")


    ]