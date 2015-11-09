from django.http import HttpResponse
from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'Inicio.html', {
        'nuevo_texto_libro': request.POST['texto_libro'],
    })