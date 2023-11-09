from django.shortcuts import render
from control_estudios.models import Estudiante, Curso

def listar_estudiantes(request):
    contexto = {
        "profesores": "Pedro y Juan", 
        "estudiantes": Estudiante.objects.all()
        }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
        )
    return http_response

def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response


def crear_curso(request):
    if request.method == "POST":
        # como es post es guardado de datos
        data = request.POST  # request.POST es un diccionario

        # creo un curso en memoria RAM
        curso = Curso(nombre=data['nombre'], comision=data['comision'])

        # lo guardo en la base de datos
        curso.save()

        # redirecciona al usuario a la lista de cursos
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)
    else:  # GET
        # descargar formulario inicial
        http_response = render(
            request=request,
            template_name='control_estudios/formulario_curso_a_mano.html',
        )
        return http_response

