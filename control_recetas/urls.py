from django.urls import path
from control_recetas.views import  buscar_receta, RecetaListView, RecetaDetailView, RecetaCreateView, RecetaUpdateView, RecetaDeleteView 

urlpatterns = [
    path("buscar-receta/", buscar_receta, name="buscar_receta"),
    path("recetas/", RecetaListView.as_view(), name="lista_recetas"),
    path("recetas/<int:pk>/", RecetaDetailView.as_view(), name="ver_receta"),
    path("crear-receta/", RecetaCreateView.as_view(), name="crear_receta"),
    path("editar-receta/<int:pk>/", RecetaUpdateView.as_view(), name="editar_receta"),
    path("eliminar-receta/<int:pk>/", RecetaDeleteView.as_view(), name="eliminar_receta")


    ]