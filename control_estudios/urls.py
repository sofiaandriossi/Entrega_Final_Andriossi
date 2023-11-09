from django.urls import path
from control_estudios.views import listar_estudiantes, crear_curso, listar_cursos

urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes" ),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("cursos/", listar_cursos, name="lista_cursos")
    ]