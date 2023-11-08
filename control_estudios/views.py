from django.shortcuts import render

def listar_estudiantes(request):
    contexto = {"estudiantes": [
        {"nombre": "Emanuel", "apellido": "Dautel"},
        {"nombre": "Manuela", "apellido": "Gomez"},
        {"nombre": "Ivan", "apellido": "Tomasevich"},
        {"nombre": "Carlos", "apellido": "Perez"},
        ]
        }
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
        )
    return http_response


