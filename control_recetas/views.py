from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



from control_recetas.models import Recetas, Usuario
from control_recetas.forms import RecetaFormulario







@login_required
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


    

class RecetaListView(ListView):
    model = Recetas
    template_name = 'control_recetas/lista_recetas.html'


class RecetaCreateView(LoginRequiredMixin, CreateView):
    model = Recetas
    fields = ('fecha', 'nombre', 'descripcion', 'ingredientes', 'autor')
    success_url = reverse_lazy('lista_recetas')
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # Agregamos la información del creador
        self.object.creador = self.request.user
        self.object.save()
        return super().form_valid(form)


class RecetaDetailView(DetailView):
    model = Recetas
    success_url = reverse_lazy('lista_recetas')


class RecetaUpdateView(LoginRequiredMixin, UpdateView):
    model = Recetas
    fields = ('nombre', 'descripcion', 'ingredientes')
    success_url = reverse_lazy('lista_recetas')


class RecetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Recetas
    success_url = reverse_lazy('lista_recetas')