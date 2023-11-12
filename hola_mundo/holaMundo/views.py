from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Hola mundo <br><br> Este es una prueba de aplicacion web con Django por Yahir Hernández")


# Create your views here.
