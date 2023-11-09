from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=25)
    apellido = forms.CharField(required=True, max_length=25)
    usuario = forms.CharField(required=True, max_length=15)
    email= forms.EmailField(max_length=50)
    fecha_nacimiento = forms.DateField()

class RecetasFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=25)
    descripcion = forms.CharField(required=True, max_length=250)
    ingredientes = forms.CharField(required=True, max_length=250)
    autor = forms.CharField(required=True)

