from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def saludar(request):
    saludo="Hola querido usuario"
    respuesta_http= HttpResponse(saludo)
    return respuesta_http

def saludar_con_fecha(request):
    hoy= datetime.now()
    saludo= f"Hola querido usuario, hoy es {hoy.day}/ {hoy.month}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_html(request):
    contexto = {"mi_nombre": "Sofía",
                "profesores": ["Pedro","Mariano", "Ruben", "Luciano"],
                "comision": "47780" ,}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
        )
    return http_response
