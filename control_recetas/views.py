from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q


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
    


def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == "POST":
        usuario.delete()
        url_exitosa = reverse('lista_usuarios')
        return redirect(url_exitosa)
    

def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == "POST":
        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            # modificamos el objeto en memoria RAM
            usuario.nombre = data['nombre']
            usuario.apellido = data['apellido']
            usuario.usuario= data["usuario"]
            # Los cambios se guardan en la Base de datos
            usuario.save()

            url_exitosa = reverse('lista_usuarios')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'usuario': usuario.usuario,
        }
        formulario = UsuarioFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_recetas/formulario_usuarios.html',
        context={'formulario': formulario},
    )

class RecetaListView(ListView):
    model = Recetas
    template_name = 'control_recetas/lista_recetas.html'


class RecetaCreateView(CreateView):
    model = Recetas
    fields = ('nombre', 'descripcion', 'ingredientes', 'autor')
    success_url = reverse_lazy('lista_recetas')


class RecetaDetailView(DetailView):
    model = Recetas
    success_url = reverse_lazy('lista_recetas')


class RecetaUpdateView(UpdateView):
    model = Recetas
    fields = ('nombre', 'descripcion', 'ingredientes')
    success_url = reverse_lazy('lista_recetas')


class RecetaDeleteView(DeleteView):
    model = Recetas
    success_url = reverse_lazy('lista_recetas')