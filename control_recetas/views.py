from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

from control_recetas.models import Recetas, Usuario
from control_recetas.forms import UsuarioFormulario, RecetaFormulario

def listar_usuarios(request):
    contexto = {
        "usuarios": Usuario.objects.all(),
        }
    http_response = render(
        request=request,
        template_name='control_recetas/lista_usuarios.html',
        context=contexto,
        )
    return http_response

def listar_recetas(request):
    contexto = {
        "recetas": Recetas.objects.all()}
    http_response = render(
        request=request,
        template_name='control_recetas/lista_recetas.html',
        context=contexto,
    )
    return http_response



def crear_usuario(request):
    if request.method == "POST":
        # Como es POST es un guardado de datos
        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            usuario = data["usuario"]
            # Se crea en memoria ram
            usuario = Usuario(nombre=nombre, apellido=apellido, usuario=usuario)
            # Se guarda en la BD
            usuario.save()

            # Redirección a la lista cursos
            url_exitosa = reverse('lista_usuarios')  # url: estudios/cursos/
            return redirect(url_exitosa)
    else:  # Como es un GET es una descarga del formulario inicial (si el formulario no es válido caemos acá)
        formulario = UsuarioFormulario()
        http_response = render(
        request=request,
        template_name='control_recetas/formulario_usuarios.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_receta(request):
    if request.method == "POST":
        # Como es POST es un guardado de datos
        formulario = RecetaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            descripcion = data["descripcion"]
            ingredientes = data["ingredientes"]
            # Se crea en memoria ram
            receta= Recetas(nombre=nombre, descripcion=descripcion, ingredientes=ingredientes)
            # Se guarda en la BD
            receta.save()

            # Redirección a la lista cursos
            url_exitosa = reverse('lista_recetas')  # url: estudios/cursos/
            return redirect(url_exitosa)
    else:  # Como es un GET es una descarga del formulario inicial (si el formulario no es válido caemos acá)
        formulario = RecetaFormulario()
        http_response = render(
        request=request,
        template_name='control_recetas/formulario_recetas.html',
        context={'formulario': formulario}
    )
    return http_response



def buscar_receta(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        recetas = Recetas.objects.filter(nombre__contains=busqueda)

        contexto = {
            "recetas": recetas,
        }
        http_response = render(
            request=request,
            template_name='control_recetas/lista_recetas.html',
            context=contexto,
        )
        return http_response
    
def buscar_usuario(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        usuarios = Usuario.objects.filter(nombre__contains=busqueda)

        contexto = {
            "usuarios": usuarios
        }
        http_response = render(
            request=request,
            template_name='control_recetas/lista_usuarios.html',
            context=contexto,
        )
        return http_response
    

def eliminar_receta(request, id):
    receta = Recetas.objects.get(id=id)
    if request.method == "POST":
        receta.delete()
        url_exitosa = reverse('lista_receta')
        return redirect(url_exitosa)