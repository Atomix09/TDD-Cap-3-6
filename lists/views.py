from django.http import HttpResponse

# Create your views here.
def pagina_inicio(request):
    return HttpResponse('<html><title>Listas de Tareas</title></html>')