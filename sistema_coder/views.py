from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {"marca": "Nutricheff"}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
        )
    return http_response

def acerca_de_mi(request):
    contexto = {"nombre": "Sofía", "apellido": "Andriossi"}
    http_response = render(
        request=request,
        template_name='acerca_de_mi.html',
        context=contexto,
        )
    return http_response



