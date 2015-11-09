from django.http import HttpResponse

# Create your views here.
def pagina_inicio(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')