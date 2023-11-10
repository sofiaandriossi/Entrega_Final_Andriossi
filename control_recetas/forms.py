from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=25)
    apellido = forms.CharField(required=True, max_length=25)
    usuario = forms.CharField(required=True, max_length=15)
class RecetaFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=25)
    descripcion = forms.CharField(required=True, max_length=250)
    ingredientes = forms.CharField(required=True, max_length=250)
    autor = forms.CharField(required=True)

